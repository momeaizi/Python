kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":

    s_kata = list()
    s_kata.append(f"module_{kata[0]:02}")
    s_kata.append(f"ex_{kata[1]:02}")
    s_kata.append(f"{kata[2]:.2f}")
    s_kata.append(f"{kata[3]:.2e}")
    s_kata.append(f"{kata[4]:.2e}")
    print(f"{s_kata[0]}, {s_kata[1]} : {s_kata[2]}, {s_kata[3]}, {s_kata[4]}")
