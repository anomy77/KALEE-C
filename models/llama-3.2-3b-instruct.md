# KALEE Model Card: LLaMA 3.2 3B Instruct

- **Base Architecture**: Meta LLaMA 3.2 (`LlamaForCausalLM`)
- **Total Parameters**: 3,212,749,824 (3.21B)
- **Layers**: 28
- **Hidden Dimension**: 3072
- **Attention Heads**: 24 Query / 8 Key-Value (GQA Ratio: 3:1)
- **Head Dimension**: 128
- **Context Capacity**: 2048 tokens
- **Vocabulary Size**: 128,256 tokens

## KALEE Precision & Memory Profile
- **Quantization Mode**: Innovation 2 Knapsack Sensitivity-Aware Auto
  - Allocated Q8_0: 70 tensors (Sensitive funnels & vocabulary head)
  - Allocated Q4_0: 70 tensors (Resilient intermediate FFN layers)
  - Allocated FP32: RMSNorm, RoPE, Control Delimiters (<think>, BOS, EOS)
- **Flash ROM Storage**: 2,570.46 MB (`weights.bin`)
- **Static RAM Footprint**: 154.28 MB (Zero dynamic allocations, `malloc = 0`)
- **Real-Time Timing ($T_{\text{WCET}}$)**: 48.43 ms / token (ISO 26262 ASIL-D Compliant $\le 50.00\text{ ms}$)

## Release Artifacts
- Native Binary: `model_llama_3_2_3b_kalee.exe`
- Flash Weights: `weights.bin`
