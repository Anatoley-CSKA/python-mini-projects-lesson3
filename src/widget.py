from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    words = info.split()
    if len(words) < 2:
        raise ValueError("Неверный формат строки: должно быть 'тип номер'")
    type_part = ' '.join(words[:-1])
    number = words[-1]
    if number.isdigit():
        if len(number) == 16:
            masked = get_mask_card_number(number)
        elif len(number) >= 4:
            masked = get_mask_account(number)
        else:
            raise ValueError("Номер слишком короткий")
        return f"{type_part} {masked}"
    else:
        raise ValueError("Номер должен содержать только цифры")

def get_date(date_str: str) -> str:
    from datetime import datetime
    date_part = date_str.split("T")[0]
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    return dt.strftime("%d.%m.%Y")
