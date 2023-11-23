import csv

def create_vcf_file(input_csv_file, output_vcf_file):
    with open(input_csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open(output_vcf_file, 'w') as vcf_file:
            # Skip the first row (header)
            next(csv_reader, None)

            for row in csv_reader:
                if len(row) >= 2:  # Ensure there are at least 2 columns
                    name = row[0]
                    phone_number = row[1]

                    # Check if both name and phone number are not empty
                    if name and phone_number:
                        vcf_file.write(f"BEGIN:VCARD\n")
                        vcf_file.write(f"VERSION:3.0\n")
                        vcf_file.write(f"N:{name};;;\n")
                        vcf_file.write(f"TEL;TYPE=CELL:{phone_number}\n")
                        vcf_file.write(f"END:VCARD\n")

if __name__ == '__main__':
    create_vcf_file('CORE MLSC.csv', 'TRY4.vcf')

