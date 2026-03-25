import requests
import csv

HOST = "http://jcssdev.pythonanywhere.com/"


def main():
	with open("bugs.csv", "w") as f:
		csv_writer = csv.writer(f)
		# csv header
		csv_writer.writerow(["id", "package", "status", "summary"])
		url = HOST + "bugs" # page 1
		while url:
			response = requests.get(url)
			json_resp = response.json()
			url = json_resp["next"]
			for r in json_resp["results"]:
				csv_writer.writerow([r["id"], r["package"], r["status"], r["summary"]])

	print("FINISHED!")
if __name__ == '__main__':
	main()