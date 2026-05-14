#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SIGNATURE_PREFIX = "safemed-mobile-data-package-v1:"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare GitHub Release assets for the SafeMed mobile data package.")
    parser.add_argument("--package-dir", type=Path, required=True, help="Directory from build_mobile_safety_package.py")
    parser.add_argument("--output-dir", type=Path, required=True, help="Release asset output directory")
    parser.add_argument("--repo", default="ctshieh/ai-pharmacist-taiwan-data")
    parser.add_argument("--release-tag", required=True)
    parser.add_argument("--minimum-app-version", default="0.1.0")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def mvp_signature(sha256_hex: str) -> str:
    return hashlib.sha256(f"{SIGNATURE_PREFIX}{sha256_hex}".encode("utf-8")).hexdigest()


def read_manifest(package_dir: Path) -> dict[str, Any]:
    manifest_path = package_dir / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def release_download_url(repo: str, tag: str, filename: str) -> str:
    return f"https://github.com/{repo}/releases/download/{tag}/{filename}"


def build_public_manifest(manifest: dict[str, Any], gzip_path: Path, repo: str, release_tag: str, minimum_app_version: str) -> dict[str, Any]:
    gzip_sha256 = sha256_file(gzip_path)
    expected_gzip_sha256 = manifest.get("gzip_sha256")
    if expected_gzip_sha256 and expected_gzip_sha256 != gzip_sha256:
        raise RuntimeError("gzip sha256 does not match source manifest")

    return {
        "package_id": manifest.get("package_id", "safemed-taiwan-mobile-safety-sqlite"),
        "version": manifest.get("version", release_tag),
        "created_at": manifest.get("created_at", datetime.now(timezone.utc).isoformat()),
        "minimum_app_version": minimum_app_version,
        "package_url": release_download_url(repo, release_tag, gzip_path.name),
        "package_format": "sqlite-gzip",
        "package_media_type": "application/gzip",
        "content_encoding": "gzip",
        "sha256": gzip_sha256,
        "sqlite_sha256": manifest.get("sqlite_sha256"),
        "sqlite_bytes": manifest.get("sqlite_bytes"),
        "gzip_bytes": gzip_path.stat().st_size,
        "signature": mvp_signature(gzip_sha256),
        "signature_algorithm": "MVP_SHA256_PREFIX_SIGNATURE",
        "signature_payload_prefix": SIGNATURE_PREFIX,
        "production_signature_note": "正式版需改為 Ed25519/RSA detached signature，App 內建 public key 驗證。",
        "tables": manifest.get("tables", {}),
        "safety_contract": manifest.get("safety_contract", {}),
        "data_sources": [
            {
                "source_id": "SAFE_MED_TAIWAN_PUBLIC_RELEASE",
                "display_name": "AI 藥師的呢喃台灣公開手機資料包",
                "license": "依 DATA_SOURCES.md、NOTICE.md 與各來源資料授權條款使用。",
                "use": "手機本機藥品正規化、重複成分偵測與保守用藥安全提醒。",
            }
        ],
        "privacy_notice": "手機下載本資料包不需要上傳藥單；使用者藥單預設留在手機本機。",
    }


def write_checksums(output_dir: Path, paths: list[Path]) -> None:
    lines = [f"{sha256_file(path)}  {path.name}" for path in paths if path.exists()]
    (output_dir / "checksums.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_release_notes(output_dir: Path, public_manifest: dict[str, Any]) -> None:
    counts = public_manifest.get("tables", {})
    lines = [
        f"# {public_manifest['version']}",
        "",
        "這是 AI 藥師的呢喃免費版手機離線資料包。",
        "",
        "## 內容",
        "",
    ]
    for table, count in counts.items():
        lines.append(f"- `{table}`: {count}")
    lines.extend(
        [
            "",
            "## 限制",
            "",
            "- 本資料包不是完整商用藥物交互作用資料庫。",
            "- 若資料不足或藥品無法確認，App 必須保守提醒使用者詢問藥師或醫師。",
            "- 不得根據 App 自行停藥、減藥或換藥。",
            "",
            "## 驗證",
            "",
            f"- SHA-256: `{public_manifest['sha256']}`",
            f"- Signature algorithm: `{public_manifest['signature_algorithm']}`",
        ]
    )
    (output_dir / "release_notes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = read_manifest(args.package_dir)
    gzip_name = str(manifest.get("gzip_file") or "mobile_safety_package.sqlite3.gz")
    gzip_path = args.package_dir / gzip_name
    if not gzip_path.exists():
        raise FileNotFoundError(f"gzip package not found: {gzip_path}")

    public_manifest = build_public_manifest(
        manifest,
        gzip_path,
        args.repo,
        args.release_tag,
        args.minimum_app_version,
    )

    output_gzip_path = args.output_dir / gzip_path.name
    shutil.copy2(gzip_path, output_gzip_path)
    manifest_output_path = args.output_dir / "manifest.json"
    manifest_output_path.write_text(json.dumps(public_manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    notice_source = Path(__file__).resolve().parents[1] / "NOTICE.md"
    notice_output_path = args.output_dir / "NOTICE.md"
    shutil.copy2(notice_source, notice_output_path)

    sqlite_path = args.package_dir / str(manifest.get("sqlite_file") or "mobile_safety_package.sqlite3")
    checksum_paths = [manifest_output_path, output_gzip_path]
    if sqlite_path.exists():
        checksum_paths.append(sqlite_path)
    write_checksums(args.output_dir, checksum_paths)
    write_release_notes(args.output_dir, public_manifest)

    print(json.dumps({"output_dir": str(args.output_dir), "assets": [path.name for path in args.output_dir.iterdir()]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
