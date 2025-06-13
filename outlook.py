[INFO] Setting Orion's home directory...
[INFO] Current directory set to: C:\Orion\text-generation-webui

[INFO] Activating Python virtual environment from 'installer_files'...
'.\installer_files\env\Scripts\activate.bat' is not recognized as an internal or external command,
operable program or batch file.

[INFO] Executing one_click.py with direct arguments for Orion...
21:15:00-510770 INFO     Starting Text generation web UI
21:15:00-885880 INFO     Loading "openhermes-2.5-mistral-7b.Q4_K_M.gguf"
21:15:00-908934 INFO     Using gpu_layers=33 | ctx_size=8192 | cache_type=fp16
warning: no usable GPU found, --gpu-layers option will be ignored
warning: one possible reason is that llama.cpp was compiled without GPU support
warning: consult docs/build.md for compilation instructions
build: 1 (e4c2f31) with MSVC 19.29.30159.0 for x64
system info: n_threads = 14, n_threads_batch = 14, total_threads = 20

system_info: n_threads = 14 (n_threads_batch = 14) / 20 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | LLAMAFILE = 1 | OPENMP = 1 | AARCH64_REPACK = 1 |

Web UI is disabled
main: binding port with default address family
main: HTTP server is listening, hostname: 127.0.0.1, port: 51389, http threads: 19
main: loading model
llama_model_loader: loaded meta data with 20 key-value pairs and 291 tensors from user_data\models\openhermes-2.5-mistral-7b.Q4_K_M.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = teknium_openhermes-2.5-mistral-7b
llama_model_loader: - kv   2:                       llama.context_length u32              = 32768
llama_model_loader: - kv   3:                     llama.embedding_length u32              = 4096
llama_model_loader: - kv   4:                          llama.block_count u32              = 32
llama_model_loader: - kv   5:                  llama.feed_forward_length u32              = 14336
llama_model_loader: - kv   6:                 llama.rope.dimension_count u32              = 128
llama_model_loader: - kv   7:                 llama.attention.head_count u32              = 32
llama_model_loader: - kv   8:              llama.attention.head_count_kv u32              = 8
llama_model_loader: - kv   9:     llama.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  10:                       llama.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  11:                          general.file_type u32              = 15
llama_model_loader: - kv  12:                       tokenizer.ggml.model str              = llama
llama_model_loader: - kv  13:                      tokenizer.ggml.tokens arr[str,32002]   = ["<unk>", "<s>", "</s>", "<0x00>", "<...
llama_model_loader: - kv  14:                      tokenizer.ggml.scores arr[f32,32002]   = [0.000000, 0.000000, 0.000000, 0.0000...
llama_model_loader: - kv  15:                  tokenizer.ggml.token_type arr[i32,32002]   = [2, 3, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, ...
llama_model_loader: - kv  16:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  17:                tokenizer.ggml.eos_token_id u32              = 32000
llama_model_loader: - kv  18:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  19:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:   65 tensors
llama_model_loader: - type q4_K:  193 tensors
llama_model_loader: - type q6_K:   33 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_K - Medium
print_info: file size   = 4.07 GiB (4.83 BPW)
load: control-looking token:  32000 '<|im_end|>' was not control-type; this is probably a bug in the model. its type will be overridden
load: special tokens cache size = 5
load: token to piece cache size = 0.1637 MB
print_info: arch             = llama
print_info: vocab_only       = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 4096
print_info: n_layer          = 32
print_info: n_head           = 32
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: n_swa_pattern    = 1
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 4
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 14336
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 0
print_info: rope scaling     = linear
print_info: freq_base_train  = 10000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_finetuned   = unknown
print_info: ssm_d_conv       = 0
print_info: ssm_d_inner      = 0
print_info: ssm_d_state      = 0
print_info: ssm_dt_rank      = 0
print_info: ssm_dt_b_c_rms   = 0
print_info: model type       = 7B
print_info: model params     = 7.24 B
print_info: general.name     = teknium_openhermes-2.5-mistral-7b
print_info: vocab type       = SPM
print_info: n_vocab          = 32002
print_info: n_merges         = 0
print_info: BOS token        = 1 '<s>'
print_info: EOS token        = 32000 '<|im_end|>'
print_info: EOT token        = 32000 '<|im_end|>'
print_info: UNK token        = 0 '<unk>'
print_info: PAD token        = 0 '<unk>'
print_info: LF token         = 13 '<0x0A>'
print_info: EOG token        = 32000 '<|im_end|>'
print_info: max token length = 48
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors:  CPU_AARCH64 model buffer size =  3204.00 MiB
load_tensors:   CPU_Mapped model buffer size =  4165.38 MiB
........................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 8192
llama_context: n_ctx_per_seq = 8192
llama_context: n_batch       = 256
llama_context: n_ubatch      = 256
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: freq_base     = 10000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (8192) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.12 MiB
llama_kv_cache_unified:        CPU KV buffer size =  1024.00 MiB
llama_kv_cache_unified: size = 1024.00 MiB (  8192 cells,  32 layers), K (f16):  512.00 MiB, V (f16):  512.00 MiB
llama_context:        CPU compute buffer size =   280.00 MiB
llama_context: graph nodes  = 1158
llama_context: graph splits = 1
common_init_from_params: setting dry_penalty_last_n to ctx_size = 8192
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: model loaded
main: chat template, chat_template: {%- for message in messages -%}
  {{- '<|im_start|>' + message.role + '
' + message.content + '<|im_end|>
' -}}
{%- endfor -%}
{%- if add_generation_prompt -%}
  {{- '<|im_start|>assistant
' -}}
{%- endif -%}, example_format: '<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
'
main: server is listening on http://127.0.0.1:51389 - starting the main loop
21:15:27-728302 INFO     Loaded "openhermes-2.5-mistral-7b.Q4_K_M.gguf" in 26.84 seconds.
21:15:27-728302 INFO     LOADER: "llama.cpp"
21:15:27-744197 INFO     TRUNCATION LENGTH: 8192
21:15:27-744197 INFO     INSTRUCTION TEMPLATE: "ChatML"
21:15:27-744197 INFO     Loading the extension "long_term_memory"
21:15:27-760271 ERROR    Failed to load the extension "long_term_memory".
Traceback (most recent call last):
  File "C:\Orion\text-generation-webui\modules\extensions.py", line 37, in load_extensions
    extension = importlib.import_module(f"extensions.{name}.script")
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Orion\text-generation-webui\installer_files\env\Lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 936, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1074, in get_code
  File "<frozen importlib._bootstrap_external>", line 1004, in source_to_code
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\Orion\text-generation-webui\extensions\long_term_memory\script.py", line 9
    tools_path = Path(__file__).resolve().parent.parent.parent / 'orion_scripts'
    ^^^^^^^^^^
IndentationError: expected an indented block after 'try' statement on line 7

Running on local URL:  http://127.0.0.1:7860