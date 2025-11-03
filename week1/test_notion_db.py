#!/usr/bin/env python3
"""Simple test to verify Notion database creation"""

import os
from notion_client import Client

token = os.getenv('NOTION_TOKEN')
page_id = "29a41454561d809f871eef8102006369"

notion = Client(auth=token)

print("Creating test database with new API format...")
db = notion.databases.create(
    parent={"type": "page_id", "page_id": page_id},
    title=[{"type": "text", "text": {"content": "Test DB v2"}}],
    initial_data_source={
        "properties": {
            "Name": {"title": {}},
            "Status": {
                "select": {
                    "options": [
                        {"name": "Todo", "color": "gray"},
                        {"name": "Done", "color": "green"}
                    ]
                }
            }
        }
    }
)

print(f"Database created: {db['id']}")
print(f"Properties in response: {'properties' in db}")

# Retrieve the database to check properties
import json
db_retrieved = notion.databases.retrieve(db['id'])
print(f"\nRetrieved database keys: {list(db_retrieved.keys())}")
print(f"Retrieved database properties: {list(db_retrieved.get('properties', {}).keys())}")
print(f"Data sources: {db_retrieved.get('data_sources', [])}")

# Check if there's a data source with properties
if 'data_sources' in db_retrieved and len(db_retrieved['data_sources']) > 0:
    data_source_id = db_retrieved['data_sources'][0]['id']
    print(f"\nData source ID: {data_source_id}")
    # Use the data source API endpoint directly
    import httpx
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2025-09-03",  # New API version for data sources
        "Content-Type": "application/json"
    }
    try:
        response = httpx.get(
            f"https://api.notion.com/v1/data_sources/{data_source_id}",
            headers=headers
        )
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text[:500]}")
        response.raise_for_status()
        ds = response.json()
        print(f"Data source properties: {list(ds.get('properties', {}).keys())}")

        # If properties exist, try creating a page
        if 'properties' in ds and len(ds['properties']) > 0:
            print("\nCreating test page using data source properties...")
            page = notion.pages.create(
                parent={"type": "database_id", "database_id": db['id']},
                properties={
                    "Name": {"title": [{"text": {"content": "Test Item"}}]},
                    "Status": {"select": {"name": "Todo"}}
                }
            )
            print(f"✅ Page created successfully: {page['id']}")
    except Exception as e:
        print(f"Error retrieving data source: {e}")

# Try to create a page
if 'properties' in db_retrieved and len(db_retrieved['properties']) > 0:
    print("\nCreating test page...")
    page = notion.pages.create(
        parent={"type": "database_id", "database_id": db['id']},
        properties={
            "Name": {"title": [{"text": {"content": "Test Item"}}]},
            "Status": {"select": {"name": "Todo"}}
        }
    )
    print(f"Page created: {page['id']}")
else:
    print("\nNo properties found in database!")
