"""initial migration

Revision ID: 6c936912d5c1
Revises: 
Create Date: 2022-04-05 02:24:42.261684-07:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlmodel
# revision identifiers, used by Alembic.
revision = '6c936912d5c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.Column('is_superuser', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)

    op.create_table('arrangementtype',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('name_en', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('audience',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('name_en', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('icon_class', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('businesshour',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('start_of_business_hours', sa.Time(), nullable=False),
    sa.Column('end_of_business_hours', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('displaylayoutsetting',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('html_template', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('css_template', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('file_output_path', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_location_name'), 'location', ['name'], unique=False)
    op.create_table('organizationtype',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('middle_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('screengroup',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('group_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('group_name_en', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('servicetype',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('timelineevent',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(length=1024), nullable=False),
    sa.Column('stamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arrangement',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('stages', postgresql.ENUM('PLANNING', 'REQUISITIONING', 'READY_TO_LAUNCH', 'IN_PRODUCTION', name='stagechoices'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('name_en', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('starts', sa.Date(), nullable=False),
    sa.Column('ends', sa.Date(), nullable=False),
    sa.Column('arrangement_type_id', sa.Integer(), nullable=True),
    sa.Column('audience_id', sa.Integer(), nullable=True),
    sa.Column('responsible_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arrangement_type_id'], ['arrangementtype.id'], ),
    sa.ForeignKeyConstraint(['audience_id'], ['audience.id'], ),
    sa.ForeignKeyConstraint(['responsible_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('calendar',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('is_personal', sa.Boolean(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('confirmationreceipt',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('guid', sqlmodel.sql.sqltypes.AutoString(length=68), nullable=False),
    sa.Column('sent_to', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('sent_when', sa.DateTime(), nullable=True),
    sa.Column('confirmed_when', sa.DateTime(), nullable=True),
    sa.Column('requested_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['requested_by_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('guid')
    )
    op.create_index(op.f('ix_confirmationreceipt_guid'), 'confirmationreceipt', ['guid'], unique=False)
    op.create_table('displaylayout',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=1024), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('is_room_based', sa.Boolean(), nullable=False),
    sa.Column('all_events', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('setting_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['setting_id'], ['displaylayoutsetting.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('organization_number', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('organization_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organization_type_id'], ['organizationtype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person_business_hour',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('businesshour_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['businesshour_id'], ['businesshour.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('max_capacity', sa.Integer(), nullable=False),
    sa.Column('has_screen', sa.Boolean(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_name'), 'room', ['name'], unique=False)
    op.create_table('screenresource',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('name_en', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('is_room_screen', sa.Boolean(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location_id', 'name', name='uniq_name_loc_1')
    )
    op.create_table('arrangement_organization_participants',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arrangement_owners',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arrangement_people_participants',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arrangement_timeline_events',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.Column('timelineevent_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['timelineevent_id'], ['timelineevent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arrangementdisplaylayout',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('display_layout_id', sa.Integer(), nullable=False),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['display_layout_id'], ['displaylayout.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('calendar_people_resources',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('calendar_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendar.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('calendar_room_resources',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('calendar_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendar.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('displaylayoutresource',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('layout_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['screengroup.id'], ),
    sa.ForeignKeyConstraint(['layout_id'], ['displaylayout.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['screenresource.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventserie',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('arrangement_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('looseservicerequisition',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('comment', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('arrangement_id', sa.Integer(), nullable=True),
    sa.Column('type_to_order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['type_to_order_id'], ['servicetype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('note',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(length=1024), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('confirmation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['confirmation_id'], ['confirmationreceipt.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization_members',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('screenresourcegroup',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['screengroup.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['screenresource.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('serviceprovider',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('service_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('service_type_id', sa.Integer(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.ForeignKeyConstraint(['service_type_id'], ['servicetype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arrangement_notes',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.Column('all_day', sa.Boolean(), nullable=True),
    sa.Column('sequence_guid', sqlmodel.sql.sqltypes.AutoString(length=40), nullable=True),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(length=40), nullable=True),
    sa.Column('serie_id', sa.Integer(), nullable=True),
    sa.Column('arrangement_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['serie_id'], ['eventserie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization_notes',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person_notes',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_articles',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_looseservicerequisition',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('looseservicerequisition_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['looseservicerequisition_id'], ['looseservicerequisition.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_notes',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_people',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_rooms',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventdisplaylayout',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('display_layout_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['display_layout_id'], ['displaylayout.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventservice',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('receipt_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('service_provider_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['receipt_id'], ['confirmationreceipt.id'], ),
    sa.ForeignKeyConstraint(['service_provider_id'], ['serviceprovider.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventservice_associated_people',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('eventservice_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['eventservice_id'], ['eventservice.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventservice_notes',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('eventservice_id', sa.Integer(), nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['eventservice_id'], ['eventservice.id'], ),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('eventservice_notes')
    op.drop_table('eventservice_associated_people')
    op.drop_table('eventservice')
    op.drop_table('eventdisplaylayout')
    op.drop_table('event_rooms')
    op.drop_table('event_people')
    op.drop_table('event_notes')
    op.drop_table('event_looseservicerequisition')
    op.drop_table('event_articles')
    op.drop_table('person_notes')
    op.drop_table('organization_notes')
    op.drop_table('event')
    op.drop_table('arrangement_notes')
    op.drop_table('serviceprovider')
    op.drop_table('screenresourcegroup')
    op.drop_table('organization_members')
    op.drop_table('note')
    op.drop_table('looseservicerequisition')
    op.drop_table('eventserie')
    op.drop_table('displaylayoutresource')
    op.drop_table('calendar_room_resources')
    op.drop_table('calendar_people_resources')
    op.drop_table('arrangementdisplaylayout')
    op.drop_table('arrangement_timeline_events')
    op.drop_table('arrangement_people_participants')
    op.drop_table('arrangement_owners')
    op.drop_table('arrangement_organization_participants')
    op.drop_table('screenresource')
    op.drop_index(op.f('ix_room_name'), table_name='room')
    op.drop_table('room')
    op.drop_table('person_business_hour')
    op.drop_table('organization')
    op.drop_table('displaylayout')
    op.drop_index(op.f('ix_confirmationreceipt_guid'), table_name='confirmationreceipt')
    op.drop_table('confirmationreceipt')
    op.drop_table('calendar')
    op.drop_table('arrangement')
    op.drop_table('timelineevent')
    op.drop_table('servicetype')
    op.drop_table('screengroup')
    op.drop_table('person')
    op.drop_table('organizationtype')
    op.drop_index(op.f('ix_location_name'), table_name='location')
    op.drop_table('location')
    op.drop_table('displaylayoutsetting')
    op.drop_table('businesshour')
    op.drop_table('audience')
    op.drop_table('article')
    op.drop_table('arrangementtype')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###