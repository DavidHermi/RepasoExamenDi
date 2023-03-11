import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from conexionBD import conexionBD, ConexionBD


class treeview(Gtk.Window):
    def __init__(self):
        super().__init__(title="Exemplo TreeView CellRendererCombo")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        modelo = Gtk.ListStore(str, str, int)
        trvPerfilesUsuarios = Gtk.TreeView(model=modelo)
        modeloPerfis = Gtk.ListStore(str, str)

        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("DNI", celda, text=0)
        trvPerfilesUsuarios.append_column(columna)
        celda2 = Gtk.CellRendererText()
        columna2 = Gtk.TreeViewColumn("Nome", celda2, text=1)
        trvPerfilesUsuarios.append_column(columna2)

        celda3 = Gtk.CellRendererText()
        columna3 = Gtk.TreeViewColumn("perfil", celda3, text=2)
        trvPerfilesUsuarios.append_column(columna3)



        bd = conexionBD("perfisUsuarios.bd")
        conexBD = bd.conectaBD()
        cursorBD = bd.creaCursor()
        sqlUsuarios = "SELECT dni,nome  FROM usuario"
        sqlPerfisUsuario = "SELECT idPerfilFROM perfisUsuario WHERE dni=?"
        sqlPerfis = "SELECT descricion FROM perfis WHERE idperfil=?"
        lUsuarios = bd.consultaSenParametros(sqlUsuarios)
        usuariosPerfil = list()
        for usuario in lUsuarios:
            idPerfil = bd.consultaConParametros(sqlPerfisUsuario, usuario[0])
            descripcionPerfil = bd.consultaConParametros(sqlPerfis, idPerfil[0])
            elemento = list(usuario)
            elemento.append(idPerfil[0][0])
            elemento.append(descripcionPerfil[0][0])
            print(elemento)
            modelo.append(elemento)

        def on_celda3_changed(self, crCombo, fila, elemento, modeloTrv, modeloCmbPerfis):
            modeloTrv[fila][2] = modeloCmbPerfis[elemento][1]
            modeloTrv[fila][3] = modeloCmbPerfis[elemento][0]
        caixaV.pacl_start(trvPerfilesUsuarios, True, True, 0)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == '__main__':
    treeview()
    Gtk.main()