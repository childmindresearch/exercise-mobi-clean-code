def load_probabilities(file_path):
    """Loads probability values from a file into a dictionary."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    probabilities = {}
    for index, line in enumerate(lines):
        values = line.strip('\n').split(',')
        for i, value in enumerate(values):
            probabilities[i / 2] = float(value)  # i/2 accounts for the 0.5 increment
    return probabilities

def load_observations(file_path):
    """Loads observation data from a file into a list of lists."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    observations = []
    for line in lines:
        values = line.strip('\n').split(',')
        observation = [round(float(value) * 2) / 2 for value in values if value != 'NaN']
        observations.append(observation)
    return observations

def classify_observations(bird_probs, plane_probs, observations):
    """Classifies each observation based on provided probabilities."""
    classifications = []
    for observation in observations:
        plane_prob, bird_prob = calculate_initial_probabilities(bird_probs, plane_probs, observation[0])
        for speed in observation[1:]:
            plane_prob, bird_prob = update_probabilities(bird_probs, plane_probs, speed, plane_prob, bird_prob)
        
        classification = determine_classification(plane_prob, bird_prob)
        classifications.append(classification)
    return classifications

def calculate_initial_probabilities(bird_probs, plane_probs, speed):
    """Calculates initial probabilities for bird and plane based on the first observation."""
    plane_prob = plane_probs.get(speed, 0) * 0.9
    bird_prob = bird_probs.get(speed, 0) * 0.9
    total_prob = plane_prob + bird_prob
    return plane_prob / total_prob, bird_prob / total_prob

def update_probabilities(bird_probs, plane_probs, speed, plane_prob, bird_prob):
    """Updates probabilities based on a new observation."""
    new_plane_prob = plane_prob + plane_probs.get(speed, 0) * (0.9 * plane_prob + 0.1 * bird_prob)
    new_bird_prob = bird_prob + bird_probs.get(speed, 0) * (0.9 * bird_prob + 0.1 * plane_prob)
    total_prob = new_plane_prob + new_bird_prob
    return new_plane_prob / total_prob, new_bird_prob / total_prob

def determine_classification(plane_prob, bird_prob):
    """Determines the final classification based on the probabilities."""
    if plane_prob > bird_prob + 0.10:
        return f"Aircraft = {plane_prob}"
    elif bird_prob > plane_prob + 0.05:
        return f"Bird = {bird_prob}"
    else:
        return "Could not be determined."

def main():
    bird_probs = load_probabilities("pdf.txt")
    plane_probs = load_probabilities("pdf.txt")  # Assuming both bird and plane probabilities are in the same file for simplicity; adjust if they're in separate files
    observations = load_observations("data.txt")
    
    classifications = classify_observations(bird_probs, plane_probs, observations)
    for i, classification in enumerate(classifications, 1):
        print(f"[{i}]: {classification}")

if __name__ == "__main__":
    main()
