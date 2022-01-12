from flask import Blueprint

from controllers.controller import delete, index, store, show, update, delete

module_blueprint = Blueprint('module_blueprint', __name__)

mp = module_blueprint


mp.route('/', methods=['GET'])(index)
mp.route('/create', methods=['POST'])(store)
mp.route('/<int:model_id>', methods=['GET'])(show)
mp.route('/<int:model_id>/edit', methods=['POST'])(update)
mp.route('/<int:model_id>', methods=['DELETE'])(delete)