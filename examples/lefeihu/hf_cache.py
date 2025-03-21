import os
HF_HOME = "/apdcephfs/nfs/.cache/huggingface"

def cache():
    os.environ.setdefault("HF_HOME", HF_HOME)
    env_hf_home = os.environ.get("HF_HOME", "none")
    print("ENV_HF_HOME:", env_hf_home)
    if env_hf_home == "none":
        raise EnvironmentError("HF_HOME must be set to 'none'")