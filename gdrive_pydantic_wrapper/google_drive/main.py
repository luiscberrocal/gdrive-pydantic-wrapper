from pathlib import Path
from pprint import pprint

from gdrive_pydantic_wrapper.google_drive.gdrive import GDrive


def download_demo():
    sheet = "1eY85U5N4G1lo9UbjGpkGBWk_tQPx40JM00qrtfcKrjE"


def get_credentials(root_folder: Path) -> Path:
    # global root_folder, sec_file
    sec_file = root_folder / '.envs' / 'google_drive' / 'client_secrets.json'
    if not sec_file.exists():
        raise Exception(f'{sec_file} not found.')
    return sec_file


if __name__ == '__main__':
    r_folder = Path(__file__).parent.parent.parent
    s_file = get_credentials(r_folder)

    gdrive = GDrive(secrets_file=s_file)
    do_upload = False
    if do_upload:
        fldr_id = '1sMd56o7uI9uimd5LhZqXQbywL7k9l0Nq'
        file_to_upload = r_folder / 'README.md'

        gdrive.upload(file_to_upload, fldr_id)

        results = gdrive.list_content(fldr_id)
        for r in results:
            pprint(r)
            print('-' * 80)
    file_id = "1eY85U5N4G1lo9UbjGpkGBWk_tQPx40JM00qrtfcKrjE"
    gdrive.download_sheet_as_csv(file_id, 't.csv', r_folder)
