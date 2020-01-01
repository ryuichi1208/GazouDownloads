import argparse
from google_images_download import google_images_download

def main():
    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keywords', help='Set keywords: e.g. key A, key B, key C')
    parser.add_argument('-l', '--limit', help='Number of images to download')
    args = parser.parse_args()

    response = google_images_download.googleimagesdownload()

    arguments = {
        'keywords': args.keywords,
        'limit': args.limit,
        'chromedriver': '/usr/bin/chromedriver'
    } 

    paths = response.download(arguments)

if __name__ == '__main__':
    main()
