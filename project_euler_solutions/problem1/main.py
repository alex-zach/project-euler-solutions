from typing import List


def multiplies_of(of: int, start: int = 1, end: int = 1000) -> List[int]:
    return list(range((start // of + 1) * of, end, of))

def main() -> None:
    print(
        sum( # sum the set
            set( # create set of the list to remove duplicates
                multiplies_of(3,1,1000) + multiplies_of(5,1,1000) # generate list of all multiplies of 3 and 5
            ))
    )

if __name__ == "__main__":
    main()