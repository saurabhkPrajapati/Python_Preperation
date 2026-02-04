import os
import re
import csv
import glob
import shutil
import time
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
from zipfile import ZipFile


def make_directries(path_str: str):
    if not os.path.exists(path_str):
        os.makedirs(path_str)


def unzip_files_ftp():
    paths = glob.glob(rf"D:\IdaProjects\TEST_{county}\{year}\*\*\*.zip")
    for temp_path in paths:
        try:
            with ZipFile(temp_path, 'r') as zip_Object:
                # Extracting all the members of the zip
                # into a specific location.
                final_path = temp_path.rsplit('\\', 1)[0]
                if 'home' not in os.listdir(final_path):
                    zip_Object.extractall(path=final_path)
        except (Exception,) as e:
            print(temp_path, e)


def copy_output_files_ftp():
    source = rf"D:\IdaProjects\TEST_{county}\{year}\*\*\*\ubuntu\GENERAL_OUTPUT\{state}_{county}"
    source1 = rf"D:\IdaProjects\TEST_{county}\{year}\*\*\*\*\ubuntu\GENERAL_OUTPUT\{state}_{county}"

    paths = glob.glob(f"{source}\\*")
    paths1 = glob.glob(f"{source1}\\*")
    paths.extend(paths1)
    for temp_path in paths:
        temp_value1 = temp_path.split("\\")[4]
        temp_value2 = temp_path.split("\\")[5]
        destination = f"D:\\IdaProjects\\TEST_{county}\\{county.lower()}_{year}\\{temp_value1}\\{temp_value2}"
        make_directries(destination)
        temp_paths_new = glob.glob(f"{temp_path}\\*\\*")
        for file_or_fol in temp_paths_new:
            temp_ff = file_or_fol.split('\\')[-1]
            if not os.path.exists(f"{destination}\\{temp_ff}"):
                try:
                    if os.path.isdir(file_or_fol):
                        shutil.copytree(file_or_fol, f"{destination}\\PDF_FILES")
                    elif os.path.isfile(file_or_fol) and "_Logs" not in file_or_fol:
                        shutil.copy(file_or_fol, destination)
                except (Exception,) as e:
                    print(e)


def merge_total_status_csv_ftp():
    try:
        base_folder = rf'D:\IdaProjects\TEST_{county}\{county.lower()}_{year}'
        csv_list = glob.glob(f"{base_folder}\\*\\*\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv")
        status_df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
        status_output = f"{base_folder}\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv"
        status_df.to_csv(status_output, index=False)
    except (Exception,) as e:
        print(e)


# For E Drive
def redefine():
    download_folder = f"E:\\{county.upper()}"
    csv_list = glob.glob(f"{download_folder}\\*\\*\\*\\*_{county.upper()}_OUTPUT.csv")
    csv_list.extend(glob.glob(f"{download_folder}\\*\\*\\*\\*\\*\\*_{county.upper()}_OUTPUT.csv"))
    for one_csv in csv_list:
        over_write_csv = False
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            grantor = row["Grantor"]
            if isinstance(grantor, str):
                if '|I|n|d|e|x' in grantor:
                    print(one_csv)
                    over_write_csv = True
                    grantor_modify = grantor.split('|I|n|d|e|x')[0]
                    df.loc[index, 'Grantor'] = grantor_modify

        if over_write_csv:
            df.to_csv(one_csv, index=False)


def merge_total_status_csv_server():
    base_folder = rf'D:\IdaProjects\TEST_{county}\{county}_{year}\GENERAL_OUTPUT\OH_{county}'
    csv_list = glob.glob(f"{base_folder}\\*\\*\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv")
    df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
    df.astype(str).fillna('', inplace=True)
    final_output = f"{base_folder}\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv"
    df.to_csv(final_output, index=False)


def merge_year_output_csvs_ftp():
    base_folder = rf'D:\IdaProjects\TEST_{county}\{county.lower()}_{year}'
    csv_list = glob.glob(f"{base_folder}\\*\\*\\*_{county}_OUTPUT.csv")
    df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
    df.astype(str).fillna('', inplace=True)
    final_output = f"{base_folder}\\FULL_OUTPUT.csv"
    df.to_csv(final_output, index=False)


def merge_year_output_csvs_server():
    base_folder = rf'D:\IdaProjects\TEST_{county}\{county}_{year}\GENERAL_OUTPUT\OH_{county}'
    csv_list = glob.glob(f"{base_folder}\\*\\*\\*_{county}_OUTPUT.csv")
    df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
    df.astype(str).fillna('', inplace=True)
    final_output = f"{base_folder}\\FULL_OUTPUT.csv"
    df.to_csv(final_output, index=False)


def find_duplicates():
    df = pd.read_csv(r'D:\IdaProjects\TEST_DELAWARE\delaware_2001\GENERAL_OUTPUT\OH_DELAWARE\FULL_OUTPUT_ALL.csv')
    df.fillna("", inplace=True)
    duplicates = df[df.duplicated(keep='first')]
    print("Duplicate Rows :", duplicates[['Recording Date', 'Document Number', 'Document Type', 'PDF Status']])


def rename_duplicates_server():
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    csv_list = glob.glob(f"{download_folder}\\*\\*\\*\\*\\*_{county.upper()}_OUTPUT.csv")
    for one_csv in csv_list:
        over_write_csv = False
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            doc_val = row["Document Number"]
            if len(doc_val.split('_')[-1]) > 2:
                over_write_csv = True
                print(doc_val)
                new_doc_val = doc_val.split('_')[0] + '_' + doc_val.split('_')[-1][0:2]
                new_doc_pdf = doc_val.split('_')[0] + '_' + doc_val.split('_')[-1][0:2] + '.pdf'
                df.loc[index, 'Document Number'] = new_doc_val
                df.loc[index, 'PDF Name'] = new_doc_pdf

        if over_write_csv:
            df.to_csv(one_csv, index=False)


def rename_pdfs_server():
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    pdf_list = glob.glob(f"{download_folder}\\*\\*\\*\\*\\PDF_FILES\\*.pdf")
    for one_pdf_path in pdf_list:
        if len(one_pdf_path.split('\\')[-1].split('_')[-1].replace('.pdf', '')) > 2:
            print(one_pdf_path)
            new_pdf_name = one_pdf_path.split('\\')[-1].split('_')[0] + '_' + one_pdf_path.split('\\')[-1].split('_')[
                                                                                  -1][0:2] + '.pdf'
            pdf_new_path = one_pdf_path.replace(one_pdf_path.split('\\')[-1], new_pdf_name)
            os.rename(one_pdf_path, pdf_new_path)


def rename_duplicates_ftp():
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    csv_list = glob.glob(f"{download_folder}\\*\\*\\*_{county.upper()}_OUTPUT.csv")
    for one_csv in csv_list:
        over_write_csv = False
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            doc_val = row["Document Number"]
            if len(doc_val.split('_')[-1]) > 2:
                over_write_csv = True
                print(doc_val)
                new_doc_val = doc_val.split('_')[0] + '_' + doc_val.split('_')[-1][0:2]
                new_doc_pdf = doc_val.split('_')[0] + '_' + doc_val.split('_')[-1][0:2] + '.pdf'
                df.loc[index, 'Document Number'] = new_doc_val
                df.loc[index, 'PDF Name'] = new_doc_pdf

        if over_write_csv:
            df.to_csv(one_csv, index=False)


def rename_pdfs_ftp():
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    pdf_list = glob.glob(f"{download_folder}\\*\\*\\PDF_FILES\\*.pdf")
    for one_pdf_path in pdf_list:
        if len(one_pdf_path.split('\\')[-1].split('_')[-1].replace('.pdf', '')) > 2:
            print(one_pdf_path)
            new_pdf_name = one_pdf_path.split('\\')[-1].split('_')[0] + '_' + one_pdf_path.split('\\')[-1].split('_')[
                                                                                  -1][0:2] + '.pdf'
            one_pdf_path.replace(one_pdf_path.split('\\')[-1], new_pdf_name)
            os.rename(one_pdf_path, one_pdf_path)


def get_missing_pdf_ftp(year):
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    outname = f"{download_folder}\\missing_pdf.csv"
    csv_list = glob.glob(f"{download_folder}\\*_OUTPUT.csv")
    for one_csv in csv_list:
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            if row["PDF Status"] == "Y":
                pdf_name = row["Document Number"] + ".pdf"
                recording_date = str(row['Recording Date'])
                recording_date = recording_date if recording_date.startswith('0') else \
                    recording_date if recording_date.split('/')[0] in ['10', '11', '12'] else "0" + recording_date
                recording_date_folder = recording_date.replace('/', '') + "-" + recording_date.replace('/', '')
                pdf_list = glob.glob(
                    f"{download_folder}\\*\\{recording_date_folder}\\PDF_FILES\\*.pdf")
                pdf_list = [one_pdf.split('\\')[-1] for one_pdf in pdf_list]
                if pdf_name not in pdf_list:
                    print(pdf_name)
                    with open(outname, "a", newline="") as wd:
                        wr = csv.writer(wd)
                        wr.writerow([row["Document Number"], recording_date])
                        wd.close()
    print(f"Process Completed For Year -- {year} for {get_missing_pdf_ftp}")


def get_extra_pdf_ftp(year):
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    outname = f"{download_folder}\\extra_pdf.csv"
    csv_list = glob.glob(f"{download_folder}\\*_OUTPUT.csv")
    for one_csv in csv_list:
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            if row["PDF Status"] == "N":
                pdf_name = row["Document Number"] + ".pdf"
                recording_date = str(row['Recording Date'])
                recording_date = recording_date if recording_date.startswith('0') else \
                    recording_date if recording_date.split('/')[0] in ['10', '11', '12'] else "0" + recording_date
                recording_date_folder = recording_date.replace('/', '') + "-" + recording_date.replace('/', '')
                pdf_list = glob.glob(
                    f"{download_folder}\\*\\{recording_date_folder}\\PDF_FILES\\*.pdf")
                pdf_list = [one_pdf.split('\\')[-1] for one_pdf in pdf_list]
                if pdf_name in pdf_list:
                    print(pdf_name)
                    with open(outname, "a", newline="") as wd:
                        wr = csv.writer(wd)
                        wr.writerow([row["Document Number"], recording_date])
                        wd.close()


def get_missing_pdf_server(year):
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    outname = f"{download_folder}\\missing_pdf.csv"
    csv_list = glob.glob(f"{download_folder}\\*\\*\\*\\*\\*_{county.upper()}_OUTPUT.csv")
    for one_csv in csv_list:
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            if row["PDF Status"] == "Y":
                pdf_name = row["Document Number"] + ".pdf"
                recording_date = str(row['Recording Date'])
                recording_date = recording_date if recording_date.startswith('0') else \
                    recording_date if recording_date.split('/')[0] in ['10', '11', '12'] else "0" + recording_date
                recording_date_folder = recording_date.replace('/', '') + "-" + recording_date.replace('/', '')
                pdf_list = glob.glob(
                    f"{download_folder}\\*\\*\\*\\{recording_date_folder}\\PDF_FILES\\*.pdf")
                pdf_list = [one_pdf.split('\\')[-1] for one_pdf in pdf_list]
                if pdf_name not in pdf_list:
                    print(pdf_name)
                    with open(outname, "a", newline="") as wd:
                        wr = csv.writer(wd)
                        wr.writerow([row["Document Number"], recording_date])
                        wd.close()

    print(f"Process Completed For Year -- {year} for {get_missing_pdf_server}")


def get_extra_pdf_server(year):
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    outname = f"{download_folder}\\extra_pdf.csv"
    csv_list = glob.glob(f"{download_folder}\\*\\*\\*\\*\\*_{county.upper()}_OUTPUT.csv")
    for one_csv in csv_list:
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            if row["PDF Status"] == "N":
                pdf_name = row["Document Number"] + ".pdf"
                recording_date = str(row['Recording Date'])
                recording_date = recording_date if recording_date.startswith('0') else \
                    recording_date if recording_date.split('/')[0] in ['10', '11', '12'] else "0" + recording_date
                recording_date_folder = recording_date.replace('/', '') + "-" + recording_date.replace('/', '')
                pdf_list = glob.glob(
                    f"{download_folder}\\*\\*\\*\\{recording_date_folder}\\PDF_FILES\\*.pdf")
                pdf_list = [one_pdf.split('\\')[-1] for one_pdf in pdf_list]
                if pdf_name in pdf_list:
                    print(pdf_name)
                    with open(outname, "a", newline="") as wd:
                        wr = csv.writer(wd)
                        wr.writerow([row["Document Number"], recording_date])
                        wd.close()


def check_n_status_server_delaware():
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    outname = f"{download_folder}\\check_n_status_server_delaware.csv"
    csv_list = glob.glob(f"{download_folder}\\*\\*\\*\\*\\*_{county.upper()}_OUTPUT.csv")
    for one_csv in csv_list:
        df = pd.read_csv(one_csv, index_col=False, dtype=str)
        for index, row in df.iterrows():
            if row["PDF Status"] == "N" and (
                    row['Images'] != '' and row['Images'] != "0" and row['Images'] != '0 page'):
                pdf_name = row["Document Number"] + ".pdf"
                recording_date = str(row['Recording Date'])
                recording_date = recording_date if recording_date.startswith('0') else \
                    recording_date if recording_date.split('/')[0] in ['10', '11', '12'] else "0" + recording_date
                recording_date_folder = recording_date.replace('/', '') + "-" + recording_date.replace('/', '')
                pdf_list = glob.glob(
                    f"{download_folder}\\*\\*\\*\\{recording_date_folder}\\PDF_FILES\\*.pdf")
                pdf_list = [one_pdf.split('\\')[-1] for one_pdf in pdf_list]
                if pdf_name not in pdf_list:
                    print(pdf_name)
                    with open(outname, "a", newline="") as wd:
                        wr = csv.writer(wd)
                        wr.writerow([row["Document Number"], recording_date, row['Images']])
                        wd.close()


def butler_missing_finder():
    download_folder = f"D:\\IdaProjects\\TEST_{county.upper()}\\{county.lower()}_{year}"
    full_output = glob.glob(f"{download_folder}\\FULL_OUTPUT.csv")[0]
    total_status = glob.glob(f"{download_folder}\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv")[0]
    over_write_csv = False

    df_full_output = pd.read_csv(full_output, index_col=False, dtype=str)
    df_total_status = pd.read_csv(total_status, index_col=False, dtype=str)

    df_full_output['Recording Date'] = pd.to_datetime(df_full_output['Recording Date'], format='%m/%d/%Y')
    df_total_status['From Date'] = pd.to_datetime(df_total_status['From Date'], format='%m/%d/%Y')

    df_full_output_groupby = df_full_output.groupby([df_full_output['Recording Date'].dt.month])
    df_total_status_groupby = df_total_status.groupby([df_total_status['From Date'].dt.month])
    df_total_status1 = df_total_status.groupby['job_id']
    df_full_output1 = df_full_output.groupby['job_id']

    # for index, row in df.iterrows():
    #     doc_val = row["Document Number"]
    #     if len(doc_val.split('_')[-1]) > 2:
    #         over_write_csv = True
    #         print(doc_val)
    #         new_doc_val = doc_val.split('_')[0] + '_' + doc_val.split('_')[-1][0:2]
    #         new_doc_pdf = doc_val.split('_')[0] + '_' + doc_val.split('_')[-1][0:2] + '.pdf'
    #         df.loc[index, 'Document Number'] = new_doc_val
    #         df.loc[index, 'PDF Name'] = new_doc_pdf
    #
    # if over_write_csv:
    #     df.to_csv(one_csv, index=False)


def merge_total_status_csv_server_e():
    base_folder = rf'E:\OH_PLANT\{county}\{county}_{year}\GENERAL_OUTPUT\OH_{county}'
    csv_list = glob.glob(f"{base_folder}\\*\\*\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv")
    df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
    df.astype(str).fillna('', inplace=True)
    final_output = f"{base_folder}\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv"
    df.to_csv(final_output, index=False)


def merge_year_output_csvs_server_e():
    base_folder = rf'E:\OH_PLANT\{county}\{county}_{year}\GENERAL_OUTPUT\OH_{county}'
    csv_list = glob.glob(f"{base_folder}\\*\\*\\*_{county}_OUTPUT.csv")
    df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
    df.astype(str).fillna('', inplace=True)
    final_output = f"{base_folder}\\FULL_OUTPUT.csv"
    df.to_csv(final_output, index=False)


def unzip_files_ftp_server_e():
    paths = glob.glob(rf"E:\OH_PLANT\TEST_{county}\{year}\*\*\*.zip")
    for temp_path in paths:
        try:
            with ZipFile(temp_path, 'r') as zip_Object:
                # Extracting all the members of the zip
                # into a specific location.
                final_path = temp_path.rsplit('\\', 1)[0]
                if 'home' not in os.listdir(final_path):
                    zip_Object.extractall(path=final_path)
        except (Exception,) as e:
            print(temp_path, e)


def copy_output_files_ftp_server_e():
    source = rf"E:\OH_PLANT\TEST_{county}\{year}\*\*\*\ubuntu\GENERAL_OUTPUT\{state}_{county}"
    source1 = rf"E:\OH_PLANT\TEST_{county}\{year}\*\*\*\*\ubuntu\GENERAL_OUTPUT\{state}_{county}"

    paths = glob.glob(f"{source}\\*")
    paths1 = glob.glob(f"{source1}\\*")
    paths.extend(paths1)
    for temp_path in paths:
        temp_value1 = temp_path.split("\\")[4]
        temp_value2 = temp_path.split("\\")[5]
        destination = f"E:\\OH_PLANT\\TEST_{county}\\{county.lower()}_{year}\\{temp_value1}\\{temp_value2}"
        make_directries(destination)
        temp_paths_new = glob.glob(f"{temp_path}\\*\\*")
        for file_or_fol in temp_paths_new:
            temp_ff = file_or_fol.split('\\')[-1]
            if not os.path.exists(f"{destination}\\{temp_ff}"):
                try:
                    if os.path.isdir(file_or_fol):
                        shutil.copytree(file_or_fol, f"{destination}\\PDF_FILES")
                    elif os.path.isfile(file_or_fol) and "_Logs" not in file_or_fol:
                        shutil.copy(file_or_fol, destination)
                except (Exception,) as e:
                    print(e)


def merge_total_status_ftp_server_e():
    base_folder = rf'E:\OH_PLANT\TEST_{county}\{county}_{year}'
    csv_list = glob.glob(f"{base_folder}\\*\\*\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv")
    df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
    df.astype(str).fillna('', inplace=True)
    final_output = f"{base_folder}\\TOTAL_RECORDS_STATUS_DESCRIPTION.csv"
    df.to_csv(final_output, index=False)


def merge_year_output_ftp_server_e():
    base_folder = rf'E:\OH_PLANT\TEST_{county}\{county}_{year}'
    csv_list = glob.glob(f"{base_folder}\\*\\*\\*_{county}_OUTPUT.csv")
    df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
    df.astype(str).fillna('', inplace=True)
    final_output = f"{base_folder}\\FULL_OUTPUT.csv"
    df.to_csv(final_output, index=False)


if __name__ == '__main__':
    # county = "COLUMBIANA"
    # county = "DELAWARE"
    # county = "MEDINA"
    # county = "BUTLER"
    # county = "CLERMONT"
    # county = "GREENE"
    # county = "HAMILTON"
    # county = "HANCOCK"
    # county = "ROSS"
    # county = "MONTGOMERY"
    # county = "LORAIN"
    county = "LICKING"
    # county = "LUCAS"
    # county = "WESTMORELAND"

    year = "2007"
    state = 'OH'
    # state = 'PA'
    # drive = "D"
    drive = "E"
    if drive == "D":
        unzip_files_ftp()
        copy_output_files_ftp()
        merge_total_status_csv_ftp()
        merge_year_output_csvs_ftp()
    else:
        unzip_files_ftp_server_e()
        copy_output_files_ftp_server_e()
        merge_total_status_ftp_server_e()
        merge_year_output_ftp_server_e()

    # merge_total_status_csv_server()
    # merge_year_output_csvs_server()

    # merge_total_status_csv_server_e()
    # merge_year_output_csvs_server_e()

    # redefine()
