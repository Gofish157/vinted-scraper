from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///vinted.db", echo=True)


def upsert(parced_items: list[dict]) -> bool:
    try:    
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO items (id, status, name, size, likes, price, upload_time, item_condition, link)
                    VALUES (:id, :status, :name, :size, :likes, :price, :upload_time, :item_condition, :link)
                    ON CONFLICT(id) DO UPDATE SET
                    status = excluded.status,
                    likes = excluded.likes,
                    price = excluded.price
                """),
                parced_items
            )
        return True
    except Exception as e:
        print(e)
        return False
