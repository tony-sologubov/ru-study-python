class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        max_positive_value = 0
        indecies_of_positive = []
        for index, value in enumerate(input_list):
            if value <= 0:
                continue
            else:
                indecies_of_positive.append(index)

            if value > max_positive_value:
                max_positive_value = value

        for index in indecies_of_positive:
            input_list[index] = max_positive_value

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:

        middle_index = (len(input_list) - 1) // 2

        if middle_index < 0:
            return -1

        middle_value = input_list[middle_index]

        if query == middle_value:
            return middle_index

        if query < middle_value:
            result = ListExercise.search(input_list[: middle_index - 1], query)
            return result if result > -1 else -1
        else:
            result = ListExercise.search(input_list[middle_index + 1 :], query)
            return middle_index + 1 + result if result > -1 else -1
