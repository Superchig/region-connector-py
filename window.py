import gi
import util

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class AppWindow(Gtk.Window):
    def __init__(self, sheet, sheet_id, subsheet_name):
        Gtk.Window.__init__(self, title='Region Connector')

        self.sheet = sheet
        self.sheet_id = sheet_id
        self.subsheet_name = subsheet_name

        grid = Gtk.Grid()
        self.add(grid)

        self.input_other_ids = Gtk.Entry()
        self.region_id = Gtk.Entry()
        self.update_button = Gtk.Button.new_with_label('Update')
        self.update_button.connect("clicked", self.update_clicked)

        grid.attach(Gtk.Label(label='Region ID:'), 0, 0, 1, 1)
        grid.attach(self.region_id, 1, 0, 1, 1)
        grid.attach(Gtk.Label(label='Connecting IDs:'), 0, 1, 1, 1)
        grid.attach(self.input_other_ids, 1, 1, 1, 1)
        grid.attach(self.update_button, 0, 2, 2, 1)

    def update_clicked(self, button):
        connecting_ids = [ int(c_id) for c_id in self.input_other_ids.get_text().split() ]

        print('connecting_ids:', connecting_ids)

        # named_range_dict = self.sheet.values() \
        #     .get(spreadsheetId=self.sheet_id, range='RegionConnections') \
        #     .execute()
        # # print('named_ranges type:', type(named_range_dict['values']))
        # print('named_range_dict:', named_range_dict)

        # raw_range = named_range_dict['range']
        # limit_cells = raw_range.split('!')[1].split(':')
        # start_cell = util.split_cell(limit_cells[0])
        # end_cell = util.split_cell(limit_cells[1])

        # col_offset = start_cell[1] - 1

        values = [[1]]
        data = []
        body = {
                'valueInputOption': 'USER_ENTERED',
                'data': data
        }
        # Relative row and column offsets are hard-coded in
        # TODO: Modify offsets to use named range's limits as a base
        range_row = int(self.region_id.get_text()) + 2
        for c_id in connecting_ids:
            range_col = util.int_to_col(c_id + 1)
            range_full = f"{self.subsheet_name}!{range_col}{range_row}"
            data.append({'range': range_full, 'values': values})

        # print('data:', data)
        
        result = self.sheet.values().batchUpdate(
                spreadsheetId=self.sheet_id, body=body).execute()
        # print('result:', result)

        responses = result['responses']
        updated_cells = 0
        for resp in responses:
            updated_cells += resp['updatedCells']
        print('updated cells:', updated_cells)
