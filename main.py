import boto3
import magic

s3 = boto3.client("s3")

def detect_file_type(file_path):
    detector = magic.Magic()
    file_type = detector.from_file(file_path)
    return file_type


def main(bucket, keyName, name):
    try:
        response = s3.download_fileobj(bucket, keyName, name)
        return response

    except Exception as e:
        return f"error:{e}"
    
print(main("csvconverted123", 'binary.csv'))