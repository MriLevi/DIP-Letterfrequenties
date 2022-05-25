import sys
from generate_matrices import generate_matrices
from classifier import classifier


# Main function
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <lang1> <lang2> <file_to_classify.txt>")
        sys.exit(1)

    # Generate the matrices
    generate_matrices(sys.argv[1], sys.argv[2])

    # Classify the matrices
    classifier(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
