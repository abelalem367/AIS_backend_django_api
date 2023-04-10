class AuthRouter:
    route_app_labels = {'auth','contenttypes','sessions','admin'}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'user_db'
        return None
    
class AIS:
    route_app_labels = {'ais'}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'ais_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'ais_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'ais_db'
        return None
    
class TRAFFIC:
    route_app_labels = {'traffic'}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'traffic_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'traffic_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'traffic_db'
        return None