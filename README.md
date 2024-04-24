
## Project Overview
This project involves creating an API to fetch the latest videos from YouTube for a given tag or search query. The data is stored in a database and provided to the user via a paginated, reverse chronologically sorted GET API. The system updates continuously in the background to ensure the latest videos are fetched and stored. The project has been extended to display the results onto a dashboard.

## Tech Stack
- **Backend**: FastAPI
- **Frontend**: React.js
- **Database**: MySQL

## System Components

### 1. Background Fetcher
- Asynchronously fetches latest videos from YouTube every 10 seconds based on a predefined search query.
- **Fields Stored**:
  - Video ID
  - Title
  - Description
  - Publishing datetime
  - Thumbnails URL
  - Channel Title

### 2. Video Data API
- **Endpoint**: `GET /`
- **Description**: Returns a list of videos stored in the database, paginated and sorted in descending order by the publishing datetime.

### 3. Keys API
#### Get All keys
- **Endpoint**: `GET /key/`
- **Description**: Returns a list of all keys stored in the database, along with their status (whether they have available quota or not).

#### Add Key
- **Endpoint**: `POST /key/{api_key}`
- **Description**: Adds a key to the database.

### 4. Database Design
- **Schema**:
  - videos (title, description, published_datetime, thumbnail, channel)
  - apikeys (keyValue, active)

- **Indexing**:
  - Primary indexing on `published_datetime` in videos table for efficient sorting and retrieval.

### 5. API Key Rotation
- Supports multiple API keys to handle quota limits; rotates keys when a quota is exhausted.
- API keys are stored directly in the database, from where they are fetched and further operations are performed.
- API keys can be added via the dashboard easily.
- The background task updates the status of all the api keys on each data fetch, and the same is further reflected on the Frontend.

### 6. Dashboard
- Provides a UI to view, filter, sort the stored videos, add and view the API keys.
- The dashboard is developed with React.js.

## Screenshots

- Overview of the dashboard
<img width="776" alt="Screenshot 2024-04-24 at 10 51 18 AM" src="https://github.com/mridul549/aviato/assets/94969636/8a15d0c9-577b-435a-9bae-68dfd183d568">

- Pagination
<img width="776" alt="Screenshot 2024-04-24 at 10 51 28 AM" src="https://github.com/mridul549/aviato/assets/94969636/c2015454-76ef-4177-889c-77d5e716d63a">

- Change the page size
<img width="365" alt="Screenshot 2024-04-24 at 10 51 58 AM" src="https://github.com/mridul549/aviato/assets/94969636/deba0edb-0988-45d1-bedf-6b19e5bcd77b">

- Sort videos by published time
<img width="260" alt="Screenshot 2024-04-24 at 10 52 10 AM" src="https://github.com/mridul549/aviato/assets/94969636/674b2a28-86fe-4a66-94f3-300d4380b899">

- Add and view API Keys
<img width="776" alt="Screenshot 2024-04-24 at 10 52 21 AM" src="https://github.com/mridul549/aviato/assets/94969636/8a7b465c-778f-4844-b74e-75546515797d">

## Demo
Check the demo [here](https://drive.google.com/file/d/1Dz5nFk7gV0OyEDS948bJvTcFo4x7npGg/view?usp=sharing)

## Installation

#### Prerequisites
- Python (>=v3.9) should be installed in the system.
- MySQL should be installed in the system and should be running on the default port 3306.

#### Steps 
The commands are in respect to MacOS, and might vary for different operating systems.

- Clone the Repository:
```bash
https://github.com/mridul549/aviato.git
```

- Navigate to the `aviato` directory in your system.

- Create virtual environment
```bash
virtualenv venv
```

- Activate virtualenv, make sure you are in the root directory. 
```bash
source venv/bin/activate
```
    
- Install the dependencies
```bash
pip3 install -r requirements.txt 
```

- Run the `init.sql` file present in the root directory
```bash
mysql -u root -p < init.sql
```

or if no password is set to the DB

```bash
mysql -u root < init.sql
```

This will create a database by name `aviato` in your system. Along with this Create the tables `videos` and `apikeys`.
- Create a `.env` file in the root directory and add the following there:
```bash
MYSQL_URI=<Your MySQL URI>
```

Example URI: `mysql+pymysql://root:<password>@localhost:3306/aviato`

- Next up, head over to the dashboard to add the Google API keys. Watch the demo video to know how to do the same.

Repo:
```bash
https://github.com/mridul549/aviato-web
```

- We are all set, now run the backend and dashboard (see readme of `aviato-web` for installation)

To run backend, use the below command:
```bash
uvicorn index:app --reload
```

- Hurray!! Installation is successful.
