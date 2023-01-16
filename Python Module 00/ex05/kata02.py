kata = (2019, 9, 25, 3, 30)

if __name__ == "__main__":

    date = "{:02}/{:02}/{}".format(kata[1], kata[2], kata[0])
    time = "{:02}:{:02}".format(kata[3], kata[4])
    print(f"{date} {time}")
