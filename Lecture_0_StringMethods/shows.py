SHOWS = [
    " Transformers",
    " avatar: the last bender",
    "Laku noc dece  ",
    " Mislim o nocima "
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())


    print(cleaned_shows)
    print(', '.join(cleaned_shows))


main()        