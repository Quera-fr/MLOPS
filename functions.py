import sqlalchemy as db

class DataBase():
    def __init__(self, uri_db="postgresql://wdasmaupyjhduf:2b8b7ead8d0ed901d758c8224c05ba9eecc5c77c8f22392c51abc4ad79c4b745@ec2-54-156-185-205.compute-1.amazonaws.com:5432/d31jj2slrugha4"):
        self.url = uri_db
        self.engine = db.create_engine(self.url)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.table_names = self.engine.table_names()

    def create_table(self, name_table: str, **kwargs):
        if name_table in self.table_names:
            print(f"La table '{name_table}' existe déjà.")
            return False
        columns = [db.Column(k, v, primary_key=True) if 'id_' in k else db.Column(k, v) for k, v in kwargs.items()]
        table = db.Table(name_table, self.metadata, *columns)
        table.create(self.engine)
        self.table_names.append(name_table)
        print(f"Table '{name_table}' créée avec succès.")

    def delete_table(self, name_table: str):
        if name_table in self.table_names:
            table = self.read_table(name_table)
            table.drop(self.engine)
            self.table_names.remove(name_table)
            print(f"Table '{name_table}' supprimée avec succès.")
        else:
            print(f"La table '{name_table}' n'existe pas.")

    def read_table(self, name_table: str):
        return db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)

    def add_row(self, name_table: str, **kwargs):
        table = self.read_table(name_table)
        stmt = db.insert(table).values(**kwargs)
        self.connection.execute(stmt)
        print("Ligne ajoutée avec succès.")

    def delete_row_by_id(self, name_table: str, id_: int):
        table = self.read_table(name_table)
        stmt = db.delete(table).where(table.c.id_ == id_)
        result = self.connection.execute(stmt)
        if result.rowcount > 0:
            print(f"Ligne avec ID {id_} supprimée avec succès.")
        else:
            print(f"Aucune ligne avec ID {id_} trouvée.")

    def select_table(self, name_table: str):
        table = self.read_table(name_table)
        stm = db.select([table])
        result = self.connection.execute(stm).fetchall()
        return result

    def update_row_by_id(self, name_table: str, id_: int, **kwargs):
        table = self.read_table(name_table)
        stmt = db.update(table).where(table.c.id_ == id_).values(**kwargs)
        result = self.connection.execute(stmt)
        if result.rowcount > 0:
            print(f"Ligne avec ID {id_} mise à jour avec succès.")
        else:
            print(f"Aucune ligne avec ID {id_} trouvée.")

    def show_all_tables(self):
        if not self.table_names:
            print("Aucune table dans la base de données.")
        else:
            print("Tables présentes dans la base de données:")
            for table_name in self.table_names:
                print(table_name)