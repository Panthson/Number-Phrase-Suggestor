numbers = {
    "2": {"a", "b", "c"},
    "3": {"d", "e", "f"},
    "4": {"g", "h", "i"},
    "5": {"j", "k", "l"},
    "6": {"m", "n", "o"},
    "7": {"p", "q", "r", "s"},
    "8": {"t", "u", "v"},
    "9": {"w", "x", "y", "z"}
}
possible_words = set()
NO_VALID_WORDS = "No Valid Words"

def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def get_number_input():
    nums = input("Enter the number : ")

    assert nums.isnumeric()

    return nums

def get_all_combinations(word, nums):
    if len(nums) is 0:
        possible_words.add(word)
        return

    first_num = nums[0]
    remaining_nums = nums[1:len(nums)]
    first_num_letters = numbers[first_num]
    for letter in first_num_letters:
        get_all_combinations(word + letter, remaining_nums)

def contains_one_or_zero(nums):
    for num in nums:
        if num is "0" or num is "1":
            return True

    return False

def main():
    english_words = load_words()

    try:
        nums = get_number_input()
    except:
        print("Invalid number sequence")
        return

    if contains_one_or_zero(nums):
        print(NO_VALID_WORDS)
        return

    get_all_combinations("", nums)
    words = english_words.intersection(possible_words)
    if len(words) is 0:
        print(NO_VALID_WORDS)
        return;

    print(words)

if __name__ == '__main__':
    main()