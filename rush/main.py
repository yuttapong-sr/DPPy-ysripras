#!/usr/bin/env python3

import sys
import json
import csv
import os

DATA_FILE = "assets_data.json"

def load_from_file():
    """Bonus: โหลดข้อมูลครุภัณฑ์จากไฟล์ JSON เมื่อเริ่มต้นโปรแกรม"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"[System] Loaded {len(data)} records from '{DATA_FILE}'.")
                return data
        except Exception as e:
            print(f"[Warning] Could not load data file: {e}")
    return []

def save_to_file(assets):
    """Bonus: บันทึกข้อมูลครุภัณฑ์ลงไฟล์ JSON อัตโนมัติเมื่อมีการเปลี่ยนแปลง"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(assets, f, ensure_ascii=False, indent=4)
        print("[System] Data saved successfully to file.")
    except Exception as e:
        print(f"[Error] Could not save data: {e}")

def display_menu():
    print("\n===== ANNUAL ASSET AUDIT & INVENTORY SYSTEM =====")
    print("1. Register New Asset")
    print("2. View All Assets")
    print("3. Audit / Update Asset Status")
    print("4. Update Asset Details (Edit Name/Location/Category)")
    print("5. Delete Asset")
    print("6. Search and Audit Summary Report")
    print("7. Reset Audit Status for New Year")
    print("8. Export Data to CSV (for Excel)")
    print("9. Export Data to JSON (Backup/Custom)")
    print("10. Exit")

def add_asset(assets):
    print("\n--- Register New Asset ---")
    asset_id = input("Enter Asset ID (e.g., AST-2026-001): ").strip()
    
    for a in assets:
        if a["id"] == asset_id:
            print("Error: Asset ID already exists in the system!")
            return
            
    name = input("Enter asset name: ").strip()
    if not name:
        print("Error: Asset name cannot be empty.")
        return
        
    category = input("Enter category (e.g., IT, Furniture, Lab): ").strip()
    location = input("Enter location / room: ").strip()

    new_asset = {
        "id": asset_id,
        "name": name,
        "category": category,
        "location": location,
        "status": "Pending",
        "checker": "-"
    }
    assets.append(new_asset)
    save_to_file(assets)
    print(f"Asset '{name}' registered successfully!")

def view_assets(assets):
    print("\n--- All Assets Registry ---")
    if not assets:
        print("No assets found in the system.")
        return
    
    for a in assets:
        print(f"ID: {a['id']} | Name: {a['name']} | Category: {a['category']} | Location: {a['location']} | Status: {a['status']} | Checker: {a['checker']}")

def audit_asset(assets):
    print("\n--- Audit Asset Status ---")
    asset_id = input("Enter Asset ID to audit: ").strip()
    
    target = None
    for a in assets:
        if a["id"] == asset_id:
            target = a
            break
            
    if not target:
        print("Error: Asset ID does not exist.")
        return

    print(f"Current Asset: {target['name']} | Current Status: {target['status']}")
    print("Select new status:")
    print("1. Checked (Verified & Normal)")
    print("2. Missing (Not found)")
    print("3. Damaged (Needs repair/disposal)")
    
    choice = input("Choose status (1-3): ").strip()
    status_map = {'1': 'Checked', '2': 'Missing', '3': 'Damaged'}
    
    if choice in status_map:
        checker_name = input("Enter auditor/checker name: ").strip()
        if not checker_name:
            print("Error: Checker name cannot be empty.")
            return
            
        target['status'] = status_map[choice]
        target['checker'] = checker_name
        save_to_file(assets)
        print("Asset audit status updated successfully!")
    else:
        print("Error: Invalid status choice.")

def update_asset_details(assets):
    """ฟังก์ชันใหม่: แก้ไขข้อมูลทั่วไปของครุภัณฑ์ (ชื่อ, หมวดหมู่, สถานที่)"""
    print("\n--- Update Asset Details ---")
    asset_id = input("Enter Asset ID to update: ").strip()
    
    target = None
    for a in assets:
        if a["id"] == asset_id:
            target = a
            break
            
    if not target:
        print("Error: Asset ID does not exist.")
        return
        
    print(f"\nCurrent Details -> Name: {target['name']} | Category: {target['category']} | Location: {target['location']}")
    print("Note: Leave blank and press Enter if you do not want to change that field.")
    
    new_name = input(f"Enter new name [{target['name']}]: ").strip()
    new_category = input(f"Enter new category [{target['category']}]: ").strip()
    new_location = input(f"Enter new location [{target['location']}]: ").strip()
    
    if new_name:
        target['name'] = new_name
    if new_category:
        target['category'] = new_category
    if new_location:
        target['location'] = new_location
        
    save_to_file(assets)
    print("Asset details updated successfully!")

def delete_asset(assets):
    """ฟังก์ชันใหม่: ลบรายการครุภัณฑ์ออกจากระบบ"""
    print("\n--- Delete Asset ---")
    asset_id = input("Enter Asset ID to delete: ").strip()
    
    target = None
    for a in assets:
        if a["id"] == asset_id:
            target = a
            break
            
    if not target:
        print("Error: Asset ID does not exist.")
        return
        
    print(f"Found Asset: ID: {target['id']} | Name: {target['name']} | Location: {target['location']}")
    confirm = input("Are you sure you want to delete this asset? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        assets.remove(target)
        save_to_file(assets)
        print(f"[System] Asset '{target['name']}' has been deleted successfully!")
    else:
        print("Deletion cancelled.")

def reset_audit_year(assets):
    print("\n--- Reset Annual Audit Status ---")
    if not assets:
        print("No assets found in the system to reset.")
        return
        
    confirm = input("Are you sure you want to reset all asset statuses to 'Pending' for the new audit year? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        for a in assets:
            a['status'] = "Pending"
            a['checker'] = "-"
        save_to_file(assets)
        print("[System] All asset statuses have been successfully reset for the new audit year!")
    else:
        print("Reset operation cancelled.")

def search_and_summary(assets):
    print("\n--- Search and Audit Summary Report ---")
    if not assets:
        print("No data available for summary.")
        return
        
    total_assets = len(assets)
    checked_count = sum(1 for a in assets if a['status'] == 'Checked')
    missing_count = sum(1 for a in assets if a['status'] == 'Missing')
    pending_count = sum(1 for a in assets if a['status'] == 'Pending')
    damaged_count = sum(1 for a in assets if a['status'] == 'Damaged')
    
    progress = (checked_count / total_assets) * 100 if total_assets > 0 else 0
    
    print(f"Total Assets: {total_assets}")
    print(f" - Checked: {checked_count}")
    print(f" - Pending: {pending_count}")
    print(f" - Missing: {missing_count}")
    print(f" - Damaged: {damaged_count}")
    print(f"Audit Progress: {progress:.2f}% completed")
    
    keyword = input("Search by status (e.g., Checked, Pending) or location name (leave blank to skip): ").strip().lower()
    if keyword:
        matches = [a for a in assets if keyword in a['status'].lower() or keyword in a['location'].lower()]
        print(f"\nMatching Assets ({len(matches)}):")
        for a in matches:
            print(f"- [{a['id']}] {a['name']} | Location: {a['location']} | Status: {a['status']}")

def export_to_csv(assets):
    print("\n--- Export Assets to CSV ---")
    if not assets:
        print("No data available to export.")
        return
        
    default_filename = "assets_report.csv"
    path_input = input(f"Enter save path/filename (default: {default_filename}): ").strip()
    csv_file = path_input if path_input else default_filename
    
    try:
        with open(csv_file, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["Asset ID", "Name", "Category", "Location", "Status", "Checker"])
            for a in assets:
                writer.writerow([a['id'], a['name'], a['category'], a['location'], a['status'], a['checker']])
                
        print(f"[System] Data successfully exported to '{csv_file}'!")
    except Exception as e:
        print(f"[Error] Could not export CSV: {e}")

def export_to_json_manual(assets):
    print("\n--- Export Assets to JSON ---")
    if not assets:
        print("No data available to export.")
        return
        
    default_filename = "assets_backup.json"
    path_input = input(f"Enter save path/filename (default: {default_filename}): ").strip()
    filename = path_input if path_input else default_filename
    if not filename.endswith(".json"):
        filename += ".json"
        
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(assets, f, ensure_ascii=False, indent=4)
        print(f"[System] Data successfully exported to '{filename}'!")
    except Exception as e:
        print(f"[Error] Could not export JSON: {e}")

def main():
    assets_list = load_from_file()
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-10): ").strip()
        
        if choice == '1':
            add_asset(assets_list)
        elif choice == '2':
            view_assets(assets_list)
        elif choice == '3':
            audit_asset(assets_list)
        elif choice == '4':
            update_asset_details(assets_list)
        elif choice == '5':
            delete_asset(assets_list)
        elif choice == '6':
            search_and_summary(assets_list)
        elif choice == '7':
            reset_audit_year(assets_list)
        elif choice == '8':
            export_to_csv(assets_list)
        elif choice == '9':
            export_to_json_manual(assets_list)
        elif choice == '10':
            print("\nExiting application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please select an option between 1 and 10.")

if __name__ == "__main__":
    main()