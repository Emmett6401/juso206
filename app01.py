import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

class AddressBook:
    def __init__(self, root):
        self.root = root
        self.root.title("주소록")

        # 다이얼로그 크기 조정
        self.root.geometry("400x300")

        self.contacts = []

        # GUI 요소 설정
        self.name_label = tk.Label(root, text="이름", font=("Arial", 14))
        self.name_label.grid(row=0, column=0)

        self.phone_label = tk.Label(root, text="전화번호", font=("Arial", 14))
        self.phone_label.grid(row=1, column=0)

        self.name_entry = tk.Entry(root, font=("Arial", 14))
        self.name_entry.grid(row=0, column=1)

        self.phone_entry = tk.Entry(root, font=("Arial", 14))
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="추가", command=self.add_entry, font=("Arial", 14))
        self.add_button.grid(row=2, column=0)

        self.update_button = tk.Button(root, text="수정", command=self.update_entry, font=("Arial", 14))
        self.update_button.grid(row=2, column=1)

        self.delete_button = tk.Button(root, text="삭제", command=self.delete_entry, font=("Arial", 14))
        self.delete_button.grid(row=2, column=2)

        self.find_button = tk.Button(root, text="찾기", command=self.find_entry, font=("Arial", 14))
        self.find_button.grid(row=3, column=0)

        self.show_button = tk.Button(root, text="모두 보기", command=self.show_entries, font=("Arial", 14))
        self.show_button.grid(row=3, column=1)

        self.load_entries()
    def load_entries(self):
        if os.path.exists('address_book.csv'):
            with open('address_book.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.contacts = [row for row in reader]

    def save_entries(self):
        with open('address_book.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.contacts)

    def add_entry(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append([name, phone])
            self.save_entries()
            self.clear_entries()
            messagebox.showinfo("정보", "주소록에 추가되었습니다.")
        else:
            messagebox.showwarning("경고", "이름과 전화번호를 입력하세요.")

    def update_entry(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if not name or not phone:
            messagebox.showwarning("경고", "이름과 전화번호를 입력하세요.")
            return
        
        for contact in self.contacts:
            if contact[0] == name:
                contact[1] = phone
                self.save_entries()
                self.clear_entries()
                messagebox.showinfo("정보", "주소록이 수정되었습니다.")
                return
        messagebox.showwarning("경고", "해당 이름을 찾을 수 없습니다.")

    def delete_entry(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("경고", "삭제할 이름을 입력하세요.")
            return
        
        for contact in self.contacts:
            if contact[0] == name:
                self.contacts.remove(contact)
                self.save_entries()
                self.clear_entries()
                messagebox.showinfo("정보", "주소록에서 삭제되었습니다.")
                return
        messagebox.showwarning("경고", "해당 이름을 찾을 수 없습니다.")

    def find_entry(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showwarning("경고", "찾을 이름을 입력하세요.", parent=self.root)
            return

        found_contacts = [contact for contact in self.contacts if name in contact[0]]
        
        if found_contacts:
            entries = "\n".join([f"이름: {c[0]}, 전화번호: {c[1]}" for c in found_contacts])
            messagebox.showinfo("찾은 연락처", entries, parent=self.root)
        else:
            messagebox.showwarning("경고", "해당 이름을 찾을 수 없습니다.", parent=self.root)

    def show_entries(self):
        if not self.contacts:
            messagebox.showinfo("정보", "주소록이 비어 있습니다.")
            return
        entries = "\n".join([f"이름: {c[0]}, 전화번호: {c[1]}" for c in self.contacts])
        messagebox.showinfo("모두 보기", entries)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBook(root)
    root.mainloop()
