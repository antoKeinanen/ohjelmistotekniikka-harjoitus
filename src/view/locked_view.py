from tkinter import Frame, Listbox, Button, Label, Entry


class LockedView(Frame):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.controller = controller

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.listbox = Listbox(self)
        for _, db_name in self.controller.state.vaults:
            self.listbox.insert("end", db_name)
        self.listbox.grid(row=0, column=0, sticky="ns")
        self.listbox.bind("<<ListboxSelect>>", self._on_listbox_selection_change)

        self.create_vault_button = Button(
            self,
            text="+ Luo uusi holvi",
            command=self._on_create_vault_button_click,
        )

        if len(self.controller.state.vaults):
            self.listbox.activate(0)

            self.create_vault_button.grid(row=1, column=0, sticky="nsew")

            self.right_container = Frame(self)
            self.right_container.grid(row=0, column=1, rowspan=2)

            self.header = Label(
                self.right_container,
                textvariable=self.controller.state.vault_heading_content,
                font=("", 16),
            )
            self.header.grid(row=0, column=0, sticky="ew", pady=16)

            self.password_label = Label(self.right_container, text="Salasana:")
            self.password_label.grid(row=1, column=0, sticky="w")

            self.password_field = Entry(self.right_container, show="⏺", width=32)
            self.password_field.grid(row=2, column=0)

            self.submit_button = Button(self.right_container, text="Avaa holvi")
            self.submit_button.grid(row=3, column=0, pady=16, sticky="w")

    def _on_listbox_selection_change(self, _):
        index = self.listbox.curselection()
        if index:
            self.controller.set_active_vault(index[0])

    def _on_create_vault_button_click(self):
        self.controller.swap_to_create_vault_view()
