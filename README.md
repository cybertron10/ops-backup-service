# ops-backup-service

Small internal HTTP service for triggering ad-hoc backups of data directories
during maintenance windows.

## Endpoints

- `GET /health` - liveness check
- `POST /backup/default` - backs up the default data directory

## Running

```
pip install -r requirements.txt
python app.py
```
