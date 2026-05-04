#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📦 MINI SISTEM CLI: SORTING & SEARCHING
Struktur Modular:
  - module_sorting.py   : Algoritma pengurutan
  - module_searching.py : Algoritma pencarian
  - cli_system.py       : Antarmuka pengguna & manajemen state
"""

# =========================================================
# 📐 MODUL SORTING
# =========================================================
def bubble_sort(arr: list) -> tuple:
    """Mengurutkan dengan Bubble Sort. Mengembalikan (array_terurut, jumlah_perbandingan)"""
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, comparisons


def insertion_sort(arr: list) -> tuple:
    """Mengurutkan dengan Insertion Sort. Mengembalikan (array_terurut, jumlah_perbandingan)"""
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons


# =========================================================
# 🔍 MODUL SEARCHING
# =========================================================
def linear_search(arr: list, target: int) -> tuple:
    """Mencari target secara linear. Mengembalikan (indeks, jumlah_langkah)"""
    steps = 0
    for i, val in enumerate(arr):
        steps += 1
        if val == target:
            return i, steps
    return -1, steps


def binary_search(arr: list, target: int) -> tuple:
    """Mencari target secara biner (data wajib terurut). Mengembalikan (indeks, jumlah_langkah)"""
    steps = 0
    low, high = 0, len(arr) - 1
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps


# =========================================================
# 🖥️ MODUL CLI SYSTEM
# =========================================================
class MiniSystemCLI:
    def __init__(self):
        self.data = []
        self.is_sorted = False
        self.last_sort_algo = None

    def _parse_input(self, raw: str) -> list:
        """Helper: parsing string angka dipisah koma/spasi"""
        try:
            return [int(x.strip()) for x in raw.replace(",", " ").split() if x.strip()]
        except ValueError:
            return []

    def input_data(self):
        print("\n📥 INPUT DATA")
        raw = input("Masukkan data (pisahkan koma/spasi): ")
        parsed = self._parse_input(raw)
        if not parsed:
            print("⚠️ Input kosong atau format salah.")
            return
        self.data = parsed
        self.is_sorted = False
        self.last_sort_algo = None
        print(f"✅ {len(self.data)} data berhasil dimuat.")

    def sort_data(self):
        if not self.data:
            print("⚠️ Data kosong. Silakan input data terlebih dahulu.")
            return

        print("\n🔄 SORTING DATA")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        choice = input("Pilih algoritma (1/2): ").strip()

        if choice == "1":
            self.data, comps = bubble_sort(self.data)
            self.last_sort_algo = "Bubble Sort"
        elif choice == "2":
            self.data, comps = insertion_sort(self.data)
            self.last_sort_algo = "Insertion Sort"
        else:
            print("❌ Pilihan tidak valid.")
            return

        self.is_sorted = True
        print(f"✅ Sorting selesai menggunakan {self.last_sort_algo}")
        print(f"📊 Jumlah perbandingan: {comps}")

    def search_data(self):
        if not self.data:
            print("⚠️ Data kosong. Silakan input data terlebih dahulu.")
            return

        print("\n🔍 SEARCHING DATA")
        raw = input("Masukkan angka yang dicari: ").strip()
        if not raw.isdigit():
            print("❌ Input harus berupa angka bulat.")
            return
        target = int(raw)

        print("1. Linear Search")
        print("2. Binary Search (wajib data terurut)")
        choice = input("Pilih algoritma (1/2): ").strip()

        if choice == "1":
            idx, steps = linear_search(self.data, target)
            status = f"Ditemukan di indeks {idx}" if idx != -1 else "Tidak ditemukan"
            print(f"🔎 Linear Search  -> {status} | Langkah: {steps}")

        elif choice == "2":
            if not self.is_sorted:
                print("⚠️ Binary Search memerlukan data terurut. Melakukan sorting otomatis...")
                self.data, _ = insertion_sort(self.data)
                self.is_sorted = True
                self.last_sort_algo = "Auto-Insertion"
            idx, steps = binary_search(self.data, target)
            status = f"Ditemukan di indeks {idx}" if idx != -1 else "Tidak ditemukan"
            print(f"🔎 Binary Search -> {status} | Langkah: {steps}")
        else:
            print("❌ Pilihan tidak valid.")

    def display_data(self):
        print("\n📤 TAMPILAN DATA")
        if not self.data:
            print("   (Data masih kosong)")
        else:
            print(f"   Data     : {self.data}")
            print(f"   Status   : {'✅ Terurut' if self.is_sorted else '❌ Belum Terurut'}")
            if self.is_sorted and self.last_sort_algo:
                print(f"   Metode   : {self.last_sort_algo}")
            print(f"   Elemen   : {len(self.data)} buah")

    def run(self):
        print("🖥️  === MINI SISTEM SORTING & SEARCHING CLI ===")
        print("   Sistem modular untuk demonstrasi algoritma dasar\n")
        
        while True:
            print("\n📋 MENU UTAMA:")
            print("1. Input Data")
            print("2. Sorting Data")
            print("3. Searching Data")
            print("4. Tampilkan Data")
            print("5. Keluar")
            
            choice = input("Pilih menu (1-5): ").strip()
            
            if choice == "1": self.input_data()
            elif choice == "2": self.sort_data()
            elif choice == "3": self.search_data()
            elif choice == "4": self.display_data()
            elif choice == "5":
                print("👋 Terima kasih! Sistem ditutup.")
                break
            else:
                print("❌ Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    app = MiniSystemCLI()
    app.run()