from flask import Flask, send_file
import subprocess
import os
import datetime

app = Flask(__name__)

# Path hidden for privacy
base_dir = r'C:\Users\*****\OneDrive\Desktop\projekti portfolio\meta metriks'

@app.route('/run-report', methods=['GET'])
def run_report():
    try:
        # Run the script that generates the Excel report
        subprocess.run(['python', os.path.join(base_dir, 'show_result_code.py')], check=True)

        report_file = os.path.join(base_dir, 'ad_report.xlsx')

        # Check if the report exists
        if not os.path.exists(report_file):
            return {"status": "error", "message": "Report not found"}, 500

        # Return the generated report as a downloadable file
        return send_file(
            report_file,
            as_attachment=True,
            download_name=f"ad_report_{datetime.date.today()}.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except subprocess.CalledProcessError as e:
        # Error occurred while executing the report script
        return {"status": "error", "message": str(e)}, 500

    except Exception as e:
        # Any other error
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(port=5000)
