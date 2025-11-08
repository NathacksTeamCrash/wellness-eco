import json
from dataGenerator import generate_test_data
from firestore_client import get_db

def upload_generated_data():
    db = get_db()
    generated = json.loads(generate_test_data())["devices"]

    for entry in generated:
        doc_ref = db.collection("deviceUsage").add(entry)
        print(f"✅ Added {entry['device_name']} → {doc_ref[1].id}")

    print(f"\nUploaded {len(generated)} device records to Firestore!")

if __name__ == "__main__":
    upload_generated_data()