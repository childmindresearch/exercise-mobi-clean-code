# Naive Bayesian Classification
# Authors: [Fabio Catania](https://github.com/fabiocat93)

def read_file(file):
    """
    Reads the content of the specified file.

    Args:
        file (str): The path to the file to be read.

    Returns:
        list: A list containing the lines of the file.
    """
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def pretty_print(result):
    """
    Function to pretty print the given result list with index and value.
    
    :param result: The list of results to be pretty printed.
    :return: None
    """
    for i, res in enumerate(result):
        print("[{}]: {}".format(i + 1, res))


def classify(bird_probabilities, plane_probabilities, data_array):
    """
    Classifies data points as either aircraft or bird based on the given probabilities of each, and the data array. Returns a list of classifications for each observation.
    """
    classifications = []

    for observation in range(10):
        b_plane = []
        b_bird = []

        for _ in range(len(data_array[observation])):
            b_plane.append(0)
            b_bird.append(0)

        for index, data_point in enumerate(data_array[observation]):
            plane = plane_probabilities[data_point] * 0.9
            b_plane[index] = plane
            bird = bird_probabilities[data_point] * 0.9
            b_bird[index] = bird

            total_sum = plane + bird
            b_plane[index] = b_plane[index] / total_sum
            b_bird[index] = b_bird[index] / total_sum

            for i in range(1, len(data_array[observation])):
                plane = b_plane[i-1] + plane_probabilities[data_array[observation][i]] * \
                        (0.9 * b_plane[i-1] + 0.1 * b_bird[i-1])
                b_plane.append(plane)
                bird = b_bird[i-1] + bird_probabilities[data_array[observation][i]] * \
                       (0.9 * b_bird[i-1] + 0.1 * b_plane[i-1])
                b_bird.append(bird)

                total_sum = plane + bird
                b_plane = [prob / total_sum if prob != 0 else prob for prob in b_plane]
                b_bird = [prob / total_sum if prob != 0 else prob for prob in b_bird]

        plane_num = b_plane[-1]
        bird_num = b_bird[-1]

        if plane_num > (bird_num + 0.10):
            classifications.append("Aircraft = " + str(plane_num))
        elif bird_num > (plane_num + 0.05):
            classifications.append("Bird = " + str(bird_num))
        else:
            classifications.append("Could not be determined.")

    return classifications

def main():
    """
    A function to read from two different files, process the data, and then classify and print the result.
    """
    with open("pdf.txt", 'r') as file:
        bird_probabilities = {}
        plane_probabilities = {}
        lines = file.readlines()
        bird_line = lines[0].strip('\n').split(',')
        plane_line = lines[1].strip('\n').split(',')
        
        for i in range(0, 400):
            bird_probabilities[i * 0.5] = float(bird_line[i])
        
        for j in range(0, 400):
            plane_probabilities[j * 0.5] = float(plane_line[j])

    with open("data.txt", 'r') as file:
        data_array = [[] for _ in range(10)]
        lines = file.readlines()
        for idx, line in enumerate(lines):
            line = line.strip('\n').split(',')
            for k in range(0, 300):
                if line[k] != 'NaN':
                    new_value = round(float(line[k]) * 2) / 2
                    data_array[idx].append(new_value)

    result = classify(bird_probabilities, plane_probabilities, data_array)
    pretty_print(result)