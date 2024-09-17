

def test_read(envs_folder):
    env_file = envs_folder / 'client_secrets.json'
    token_file = env_file / 'token.pickle'
    if token_file.exists():
        token_file.unlink()

    assert env_file.exists()

