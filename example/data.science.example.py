# data.science.example.py

def do_report(data_source):
    data = fetch_data(data_source)
    parsed_data = perse_data(data)
    filtered_data = filter_data(persed_data)
    polished_data = polist_data(filtered_data)

    final_data = analyse(polished_data)

    report = Report(final_data)
    return report
