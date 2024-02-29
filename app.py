from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

@app.route('/backup', methods=['POST'])
def backup():
    # Code to initiate backup process
    perform_backup()  # Manually initiate backup
    return 'Backup process initiated'

@app.route('/backup/status', methods=['GET'])
def backup_status():
    # Code to check backup status
    return 'Backup status: In progress'  # or 'Backup status: Completed', etc.

scheduler = BackgroundScheduler()

# Define the backup job
def perform_backup():
    # Code to perform backup
    # Example: Save data to a file or database
    with open('backup.txt', 'w') as f:
        f.write('This is a backup')

    print("Backup process completed...")

# Schedule the backup job to run every hour
scheduler.add_job(perform_backup, 'interval', hours=1)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
