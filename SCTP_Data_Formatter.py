import csv
import json
import os


def read_sctp_content_from_csv(csv_file_path):
    sctp_content_list = []
    with open(csv_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sctp_content = row.get("sctp.content", "").strip('"')
            sctp_content_list.append(sctp_content)
    return sctp_content_list


def format_sctp_content(sctp_content):
    input_list = [sctp_content[i : i + 32] for i in range(0, len(sctp_content), 32)]
    formatted_output = "\n".join(
        [
            f"{i*16:07X} {' '.join([input_list[i][j:j+2] for j in range(0, len(input_list[i]), 2)])}"
            for i in range(len(input_list))
        ]
    )
    return formatted_output


def process_json_file(file_path, json_output_file):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            sctp_data = data.get("sctp", {})
            if "content" in sctp_data:
                sctp_content = sctp_data["content"]
                formatted_output = format_sctp_content(sctp_content)
                with open(json_output_file, "a") as output:
                    output.write(formatted_output)
                    output.write("\n\n")

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")


def main():
    user_choice = input("Enter 1 for CSV, 2 for JSON folder: ")
    if user_choice == "1":
        csv_file_path = input("Enter the CSV file path: ")
    elif user_choice == "2":
        folder_path = input("Enter the JSON folder path: ")
    else:
        print("Invalid choice")

    if user_choice == "1":
        sctp_content_list = read_sctp_content_from_csv(csv_file_path)
        csv_output_file = "csv_output.txt"
        open(csv_output_file, "w").close()
        for sctp_content in sctp_content_list:
            formatted_output = format_sctp_content(sctp_content)
            with open(csv_output_file, "a") as output:
                output.write(formatted_output)
                output.write("\n\n")
        print(f"CSV Output has been written to {csv_output_file}")

    if user_choice == "2":
        json_output_file = "json_output.txt"
        json_output_file = os.path.join(folder_path, json_output_file)
        open(json_output_file, "w").close()
        json_files = []
        json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
        [print(f) for f in json_files]
        for json_file in json_files:
            json_file_path = os.path.join(folder_path, json_file)
            process_json_file(json_file_path, json_output_file)
        print(f"JSON Output has been written to {json_output_file}")
    input("Press Enter to exit.")


if __name__ == "__main__":
    main()
