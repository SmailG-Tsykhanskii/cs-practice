from tablestats import *
with open(input(), encoding="utf-8") as table:
    rows = read_rows(table)
    print(len(rows))
    counts = count_types(rows)
    print(len(counts))
    print(total_minutes(rows, 'ошибка'))
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))
