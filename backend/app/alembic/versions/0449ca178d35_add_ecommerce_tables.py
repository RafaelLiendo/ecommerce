"""add ecommerce tables

Revision ID: 0449ca178d35
Revises: 91979b40eb38
Create Date: 2020-10-12 17:39:19.698361-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0449ca178d35'
down_revision = '91979b40eb38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.DECIMAL(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart_product',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'product_id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('total', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_product',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('subtotal', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'product_id')
    )
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.drop_column('user', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('address', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.alter_column('user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_table('order_product')
    op.drop_table('order')
    op.drop_table('cart_product')
    op.drop_table('product')
    # ### end Alembic commands ###
