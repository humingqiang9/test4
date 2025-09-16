class Puppet:
    """
    Класс для настройки сети с использованием Puppet.
    """

    def __init__(self, manifest_path: str = "/etc/puppet/manifests/site.pp"):
        """
        Инициализирует класс Puppet.

        Args:
            manifest_path: Путь к файлу манифеста Puppet.
        """
        self.manifest_path = manifest_path

    def apply_manifest(self) -> None:
        """
        Применяет манифест Puppet для настройки системы.
        """
        import subprocess
        try:
            # В реальной ситуации здесь должна быть команда типа:
            # subprocess.run(["puppet", "apply", self.manifest_path], check=True)
            # Для демонстрации просто имитируем выполнение
            print(f"Применение манифеста: {self.manifest_path}")
            # subprocess.run(["echo", "Применение манифеста Puppet"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при применении манифеста: {e}")

    def configure_network(self, interface: str, ip_address: str, netmask: str, gateway: str) -> None:
        """
        Создает манифест Puppet для настройки сетевого интерфейса.

        Args:
            interface: Название сетевого интерфейса (например, eth0).
            ip_address: IP-адрес для интерфейса.
            netmask: Маска подсети.
            gateway: Шлюз по умолчанию.
        """
        manifest_content = f"""
# Манифест для настройки сети
class network_config {{
  file {{ '/etc/sysconfig/network-scripts/ifcfg-{interface}':
    ensure  => file,
    content => template('network/ifcfg-{interface}.erb'),
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    notify  => Service['network'],
  }}
}}

# Определение ресурса для файла шаблона
define network::interface(
  $ipaddress,
  $netmask,
  $gateway,
) {{
  file {{ "/etc/sysconfig/network-scripts/ifcfg-${{name}}":
    ensure  => file,
    content => template('network/ifcfg.erb'),
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    notify  => Service['network'],
  }}
}}

# Использование определения
network::interface {{ '{interface}':
  ipaddress => '{ip_address}',
  netmask   => '{netmask}',
  gateway   => '{gateway}',
}}

# Управление сервисом сети
service {{ 'network':
  ensure    => running,
  enable    => true,
  hasrestart => true,
}}
"""
        try:
            with open(self.manifest_path, 'w') as f:
                f.write(manifest_content)
            print(f"Манифест для настройки сети сохранен в {self.manifest_path}")
        except IOError as e:
            print(f"Ошибка при записи манифеста: {e}")


# Пример использования
if __name__ == "__main__":
    puppet = Puppet()
    puppet.configure_network("eth0", "192.168.1.10", "255.255.255.0", "192.168.1.1")
    puppet.apply_manifest()