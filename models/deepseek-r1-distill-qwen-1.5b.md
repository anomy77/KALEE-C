# KALEE Model Card: DeepSeek-R1 Distill Qwen 1.5B

- **Base Architecture**: DeepSeek-R1 Distill Qwen 1.5B (`Qwen2ForCausalLM`)
- **Total Parameters**: 1,777,350,144 (1.78B)
- **Layers**: 28
- **Hidden Dimension**: 1536
- **Attention Heads**: 12 Query / 2 Key-Value (GQA Ratio: 6:1)
- **Head Dimension**: 128
- **Context Capacity**: 2048 tokens
- **Vocabulary Size**: 151,936 tokens

## KALEE Precision & Memory Profile
- **Quantization Mode**: Knapsack Auto Q4_0 / FP32 Delimiters
- **Flash ROM Storage**: 1,112.22 MB (`model_deepseek_r1_15b_weights.bin`)
- **Static RAM Footprint**: 95.2 MB (Zero dynamic allocations, `malloc = 0`)
- **Reasoning Format**: Supports `<think>` step-by-step deliberative reasoning tags

## Release Artifacts
- Native Binary: `model_deepseek_r1_15b.exe`
- Flash Weights: `model_deepseek_r1_15b_weights.bin`
