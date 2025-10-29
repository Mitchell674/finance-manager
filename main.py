import json
import os
from datetime import datetime

class FinanceManager:
    def __init__(self, filename="finances.json"):
        self.filename = filename
        self.load_data()
    
    def load_data(self):
        """Загрузка данных из файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            self.data = {"transactions": [], "balance": 0.0}
    
    def save_data(self):
        """Сохранение данных в файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def add_transaction(self, amount, category, transaction_type):
        """Добавление транзакции (доход/расход)"""
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "amount": amount,
            "category": category,
            "type": transaction_type
        }
        
        self.data["transactions"].append(transaction)
        
        # Обновление баланса
        if transaction_type == "доход":
            self.data["balance"] += amount
        else:
            self.data["balance"] -= amount
        
        self.save_data()
        print(f"✅ Транзакция добавлена! Текущий баланс: {self.data['balance']:.2f} ₽")
    
    def show_balance(self):
        """Показать текущий баланс"""
        print(f"\n💰 Текущий баланс: {self.data['balance']:.2f} ₽")
    
    def show_transactions(self):
        """Показать историю транзакций"""
        if not self.data["transactions"]:
            print("\n📝 История транзакций пуста")
            return
        
        print("\n📊 История транзакций:")
        print("-" * 50)
        for i, transaction in enumerate(self.data["transactions"][-10:], 1):
            sign = "+" if transaction["type"] == "доход" else "-"
            print(f"{i}. {transaction['date']} | {sign}{transaction['amount']:.2f} ₽ | "
                  f"{transaction['category']} ({transaction['type']})")

def main():
    manager = FinanceManager()
    
    while True:
        print("\n" + "="*40)
        print("      🏠 ПЕРСОНАЛЬНЫЙ ФИНАНСОВЫЙ МЕНЕДЖЕР")
        print("="*40)
        print("1. Добавить доход")
        print("2. Добавить расход")
        print("3. Показать баланс")
        print("4. Показать историю")
        print("5. Выйти")
        
        choice = input("\nВыберите действие (1-5): ").strip()
        
        if choice == "1":
            try:
                amount = float(input("Сумма дохода: "))
                category = input("Категория (зарплата, подарок, др.): ")
                manager.add_transaction(amount, category, "доход")
            except ValueError:
                print("❌ Ошибка: введите корректную сумму")
        
        elif choice == "2":
            try:
                amount = float(input("Сумма расхода: "))
                category = input("Категория (еда, транспорт, развлечения): ")
                manager.add_transaction(amount, category, "расход")
            except ValueError:
                print("❌ Ошибка: введите корректную сумму")
        
        elif choice == "3":
            manager.show_balance()
        
        elif choice == "4":
            manager.show_transactions()
        
        elif choice == "5":
            print("👋 До свидания! Данные сохранены.")
            break
        
        else:
            print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()