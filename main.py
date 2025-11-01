import pandas as pd
import os

INPUT_CSV = "input.csv"
OUTPUT_CSV = "output.csv"

def read_csv(filename: str) -> pd.DataFrame:

    # check that the file exists
    if (not os.path.isfile(filename) and filename.endswith('.csv')):
        raise BaseException("INVALID FILENAME")

    df = pd.read_csv(filename)
    return df


def main():
    df = read_csv(INPUT_CSV)
    file_writer = open(OUTPUT_CSV, 'w')
    file_writer.write(" ,")
    for column in df:
        file_writer.write(str(column) + ",")
    file_writer.write('\n')
    
    # loop over each column to check for FDs
    for outer_col, outer_series in df.items():
        file_writer.write(str(outer_col) + ',')
        tmp_arr = [] 
        for inner_col, inner_series in df.items():
            if inner_col == outer_col:
                tmp_arr.append("Trivial")
                continue

            tmp_dict = {}
            is_fd = "Accepted"
            for outer, inner in zip(outer_series.values, inner_series.values):
                
                if outer in tmp_dict.keys():
                    if tmp_dict[outer] != inner:
                        is_fd = "Denied"
                else:
                    tmp_dict[outer] = inner
            tmp_arr.append(is_fd)
        print(tmp_arr)
        for item in tmp_arr:
            file_writer.write(item + ',')
        file_writer.write('\n')
    file_writer.close()

if __name__ == "__main__":
    main()