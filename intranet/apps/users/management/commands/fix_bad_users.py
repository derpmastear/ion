# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from intranet.apps.users.models import User


class Command(BaseCommand):
    help = "Check for user objects with no DN, and delete them."

    def handle(self, **options):
        all_users = User.objects.all()
        bad_users = []
        for u in all_users:
            # ignore non-active (aka 99999) users in check
            if u.dn is None and u.is_active:
                bad_users.append(u.id)

        if not bad_users:
            self.stdout.write("No invalid users found.")
            return

        self.stdout.write("The following {} User IDs have no corresponding DN:".format(len(bad_users)))
        self.stdout.write(", ".join([str(u) for u in bad_users]))
        self.stdout.write("Delete them?")
        input("Press enter to continue, Ctrl-C to cancel..")
        for u in bad_users:
            User.objects.get(id=u).delete()

        self.stdout.write("Done.")
