import requests
import csv

HOST = "http://jcssdev.pythonanywhere.com/"


def main(resource, fields):
	with open(f"{resource}.csv", "w") as f:
		csv_writer = csv.writer(f)
		# csv header
		csv_writer.writerow(fields)
		url = HOST + resource # page 1
		while url:
			response = requests.get(url)
			json_resp = response.json()
			url = json_resp["next"]
			for r in json_resp["results"]:
				csv_writer.writerow([r[f] for f in fields])

	print("FINISHED!")
if __name__ == '__main__':
	main("bugs", ["id", "package", "status", "summary"])
	main("comments", ["id", "bug", "user", "content"])