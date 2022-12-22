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
        low_border = 0
        high_border = len(input_list) - 1

        while low_border <= high_border:
            current_index = (low_border + high_border) // 2
            current_value = input_list[current_index]

            if query == current_value:
                return current_index

            if query < current_value:
                high_border = current_index - 1
            else:
                low_border = current_index + 1

        return -1
