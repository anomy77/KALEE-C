#!/usr/bin/env python3
"""
KALEE Model Zoo Downloader & Setup CLI
Zero external dependencies (pure Python standard library).
Downloads pre-compiled native KALEE executables and zero-copy flash weights.
"""

import os
import sys
import argparse
import urllib.request
from pathlib import Path

# Registry of pre-compiled models and their release assets
MODEL_REGISTRY = {
    "llama-3.2-3b": {
        "name": "LLaMA 3.2 3B Instruct",
        "arch": "Llama 3.2",
        "params": "3.21B",
        "context": 2048,
        "static_ram_mb": 150.7,
        "exe_name": "model_llama_3_2_3b_kalee.exe",
        "weights_name": "weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
    "llama-3.2-3b-abliterated": {
        "name": "LLaMA 3.2 3B Instruct (Abliterated / Uncensored)",
        "arch": "Llama 3.2",
        "params": "3.21B",
        "context": 2048,
        "static_ram_mb": 150.7,
        "exe_name": "model_llama_3_2_3b_abliterated_kalee.exe",
        "weights_name": "weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
    "deepseek-r1-1.5b": {
        "name": "DeepSeek-R1 Distill Qwen 1.5B",
        "arch": "Qwen 2.5",
        "params": "1.78B",
        "context": 2048,
        "static_ram_mb": 95.2,
        "exe_name": "model_deepseek_r1_15b.exe",
        "weights_name": "model_deepseek_r1_15b_weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
    "deepseek-r1-llama-8b": {
        "name": "DeepSeek-R1 Distill LLaMA 8B",
        "arch": "Llama 3.1",
        "params": "8.03B",
        "context": 2048,
        "static_ram_mb": 340.5,
        "exe_name": "model_deepseek_r1_llama_8b.exe",
        "weights_name": "weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
    "deepseek-r1-qwen-7b": {
        "name": "DeepSeek-R1 Distill Qwen 7B",
        "arch": "Qwen 2.5",
        "params": "7.61B",
        "context": 2048,
        "static_ram_mb": 320.1,
        "exe_name": "model_deepseek_r1_qwen_7b.exe",
        "weights_name": "weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
    "qwen2.5-7b": {
        "name": "Qwen 2.5 7B Instruct",
        "arch": "Qwen 2.5",
        "params": "7.61B",
        "context": 2048,
        "static_ram_mb": 320.1,
        "exe_name": "model_qwen25_7b.exe",
        "weights_name": "weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
    "qwen2.5-0.5b": {
        "name": "Qwen 2.5 0.5B Instruct",
        "arch": "Qwen 2.5",
        "params": "0.49B",
        "context": 2048,
        "static_ram_mb": 42.0,
        "exe_name": "model_qwen25_05b.exe",
        "weights_name": "model_qwen25_05b_weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
    "smollm2-135m": {
        "name": "SmolLM2 135M",
        "arch": "SmolLM2",
        "params": "0.135B",
        "context": 2048,
        "static_ram_mb": 18.4,
        "exe_name": "model_smollm2_135m.exe",
        "weights_name": "model_smollm2_135m_weights.bin",
        "release_tag": "v1.0.0",
        "repo": "VYRE/kalee-models",
    },
}


def download_with_progress(url: str, output_path: Path):
    print(f"Downloading from: {url}")
    print(f"Saving to       : {output_path}")

    def reporthook(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = min(100.0, (downloaded / total_size) * 100.0)
            mb_down = downloaded / (1024 * 1024)
            mb_total = total_size / (1024 * 1024)
            sys.stdout.write(f"\rProgress: [{percent:5.1f}%] {mb_down:7.1f} / {mb_total:7.1f} MB")
            sys.stdout.flush()
        else:
            mb_down = downloaded / (1024 * 1024)
            sys.stdout.write(f"\rDownloaded: {mb_down:7.1f} MB")
            sys.stdout.flush()

    urllib.request.urlretrieve(url, output_path, reporthook=reporthook)
    print("\nDownload complete.")


def list_models():
    print("=" * 80)
    print("                    KALEE MODEL ZOO - AVAILABLE MODELS                         ")
    print("=" * 80)
    print(f"{'Key':<26} {'Name':<36} {'Params':<8} {'RAM (MB)':<10}")
    print("-" * 80)
    for key, info in MODEL_REGISTRY.items():
        print(f"{key:<26} {info['name']:<36} {info['params']:<8} {info['static_ram_mb']:<10.1f}")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Download and setup pre-compiled KALEE models.")
    parser.add_argument("--model", type=str, default=None, help="Model key to download (e.g. llama-3.2-3b)")
    parser.add_argument("--list", action="store_true", help="List all available models in the zoo")
    parser.add_argument("--output-dir", type=str, default="./bin", help="Output directory for executable and weights")
    args = parser.parse_args()

    if args.list or not args.model:
        list_models()
        if not args.model:
            print("\nUsage example:")
            print("  python download_model.py --model llama-3.2-3b")
            sys.exit(0)

    if args.model not in MODEL_REGISTRY:
        print(f"ERROR: Model '{args.model}' not found in registry.")
        list_models()
        sys.exit(1)

    info = MODEL_REGISTRY[args.model]
    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Setting up {info['name']} in: {out_dir}")
    base_url = f"https://github.com/{info['repo']}/releases/download/{info['release_tag']}"

    exe_target = out_dir / info["exe_name"]
    weights_target = out_dir / info["weights_name"]

    print(f"\n1. Fetching executable ({info['exe_name']})...")
    download_with_progress(f"{base_url}/{info['exe_name']}", exe_target)

    print(f"\n2. Fetching weights ({info['weights_name']})...")
    download_with_progress(f"{base_url}/{info['weights_name']}", weights_target)

    print("\n" + "=" * 80)
    print("SETUP SUCCESSFUL!")
    print(f"To run interactively, launch:\n  {exe_target}")
    print("=" * 80)


if __name__ == "__main__":
    main()
