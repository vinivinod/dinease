# custom_lookups.py

from django.db.models import Lookup, CharField, TextField
from django.db.models.functions import Lower
from .custom_lookups import *
class LowerRegexp(Lookup):
    lookup_name = 'lower_regexp'

    def as_sql(self, compiler, connection):
        # Use the Lower() database function to convert to lowercase
        lhs_sql, params = self.process_lhs(compiler, connection)
        lower_sql, lower_params = compiler.compile(Lower(self.rhs))
        return f"{lhs_sql} ILIKE {lower_sql}", params + lower_params

CharField.register_lookup(LowerRegexp)
TextField.register_lookup(LowerRegexp)
