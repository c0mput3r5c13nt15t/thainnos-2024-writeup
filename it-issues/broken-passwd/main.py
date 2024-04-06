import crypt

# Given hash
incomplete_hash = "$6$twIClv9oUQhfcg.G$vIX8Xpk3VAa4/Rs7LlFwLqZD3h.DIu02sbb1mQEw/WoNJqxmjzvY________qhbeo0YVOdf673vCKlKFPFEMu1"
# Given password
password = "EneMeneMu"


def hash_password(password, salt):
    return crypt.crypt(password, salt)


if __name__ == "__main__":
    # The first part of the gives hash is the salt, so we can just hash the password with the known salt
    full_hash = hash_password(password, incomplete_hash[:19])
    print(full_hash)
    print(incomplete_hash)

    flag = "THAINNOS{"
    for i in range(len(full_hash)):
        if full_hash[i] != incomplete_hash[i]:
            flag += full_hash[i]
    flag += "}"
    print(flag)
