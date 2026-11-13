# KALEE Pre-Compiled Models

This directory contains configuration, model cards, and download references for standalone KALEE neural inference engines.

Every model in this repository is ahead-of-time (AOT) compiled into an ANSI C99 native executable with strictly zero heap allocation (`malloc = 0`) and zero external dependencies.

---

## Directory Layout

To run a model, download both the executable (`.exe`) and its flash weights (`weights.bin`), placing them together in the same directory:

```text
models/
├── llama-3.2-3b/
│   ├── model_llama_3_2_3b_kalee.exe   (~2.8 MB)
│   └── weights.bin                    (~2.54 GB)
│
├── llama-3.2-3b-abliterated/
│   ├── model_llama_3_2_3b_abliterated_kalee.exe
│   └── weights.bin
│
└── deepseek-r1-1.5b/
    ├── model_deepseek_r1_15b.exe      (~1.1 GB)
    └── model_deepseek_r1_15b_weights.bin
```

---

## Available Model Weights

| Model Identifier | Base Weights | Context Window | Static RAM | Weights File |
| :--- | :--- | :--- | :--- | :--- |
| `llama-3.2-3b` | LLaMA 3.2 3B Instruct | 2048 | 150.7 MB | `weights.bin` (2.54 GB) |
| `llama-3.2-3b-abliterated` | LLaMA 3.2 3B Uncensored | 2048 | 150.7 MB | `weights.bin` (2.54 GB) |
| `deepseek-r1-1.5b` | DeepSeek-R1 Distill Qwen 1.5B | 2048 | 95.2 MB | `model_deepseek_r1_15b_weights.bin` (1.11 GB) |
| `deepseek-r1-llama-8b` | DeepSeek-R1 Distill LLaMA 8B | 2048 | 340.5 MB | `weights.bin` (5.02 GB) |
| `deepseek-r1-qwen-7b` | DeepSeek-R1 Distill Qwen 7B | 2048 | 320.1 MB | `weights.bin` (4.76 GB) |
| `qwen2.5-7b` | Qwen 2.5 7B Instruct | 2048 | 320.1 MB | `weights.bin` (4.76 GB) |
| `qwen2.5-0.5b` | Qwen 2.5 0.5B Instruct | 2048 | 42.0 MB | `model_qwen25_05b_weights.bin` (439 MB) |
| `smollm2-135m` | SmolLM2 135M | 2048 | 18.4 MB | `model_smollm2_135m_weights.bin` (116 MB) |

---

## How to Run

1. Open your terminal in the model's folder.
2. Launch the interactive chat REPL:
   ```powershell
   .\model_llama_3_2_3b_kalee.exe
   ```
3. Or pass a one-shot prompt directly:
   ```powershell
   .\model_llama_3_2_3b_kalee.exe "Explain quantum superposition in simple terms."
   ```
